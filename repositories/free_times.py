import calendar
from datetime import datetime

import arrow
import httpx

from common.utils.speed_test import speed_test
from core.config import BASE_URL
from models.free_times import FreeTime, FreeDate


class FreeTimesRepository:

    @speed_test
    async def get_free_times_for_doctor(
            self,
            filial_id,
            filial_cash_id,
            department_id,
            doctor_id,
            start=None,
            end=None
    ):
        if start is None and end is None:
            start, end = self._get_month_interval()
        elif start is None:
            start, _ = self._get_month_interval()
        elif end is None:
            _, end = self._get_month_interval()
        data = await self._get_data_for_doctor(filial_id, filial_cash_id, department_id, doctor_id, start, end)

        free_dates = [times["workDate"] for times in data["intervals"] if times["isFree"]]
        free_dates.append("20211222")
        free_dates.append("20211225")

        free_times = await self._get_free_times(
            filial_id,
            filial_cash_id,
            department_id,
            doctor_id,
            data["dname"],
            free_dates)
        return free_times

    async def _get_data_for_doctor(self, filial_id, filial_cash_id, department_id, doctor_id, start, end):
        url = f"{BASE_URL}api/reservation/schedule?st={start}&en={end}&doctor={doctor_id}&filialId={filial_id}&cashlist={filial_cash_id}&speclist={department_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        return response.json()["data"][0]

    async def _get_free_times(self, filial_id, filial_cash_id, department_id, doctor_id, doctor_name, free_dates):
        if len(free_dates):
            url = f"https://registratura.volganet.ru/api/reservation/intervals?st={free_dates[0]}&en={free_dates[-1]}&spec={department_id}&dcode={doctor_id}&filialId={filial_id}&cashlist={filial_cash_id}&inFilials={filial_id}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
            return FreeTime(
                doctor_name=doctor_name,
                free_times=self._get_free_dates(response.json()["data"])
            )
        return FreeTime(
            doctor_name=doctor_name,
            free_times=[]
        )

    def _get_month_interval(self):
        today = datetime.now()
        start = arrow.get(f"{today.year}-{today.month}-01").format("YYYYMMDD")
        next_year = today.year
        next_month = today.month + 1
        if next_month % 12 == 1:
            next_year += 1
            next_month = 1
        next_day = calendar.monthrange(next_year, next_month)[1]
        end = arrow.get(f"{next_year}-{next_month}-{next_day}").format("YYYYMMDD")

        return start, end

    def _get_free_dates(self, dates):
        free_dates = []
        for i in range(0, len(dates)):
            date = dates[i]["workdates"][0]
            for key, value in date.items():
                free_dates.append(FreeDate(
                    date=key,
                    times=[interval["time"] for interval in value[0]["intervals"] if interval["isFree"]]
                ))

        return free_dates

