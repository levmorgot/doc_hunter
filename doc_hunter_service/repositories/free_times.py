import calendar
from datetime import datetime
from typing import List

import arrow
import httpx

from common.utils.speed_test import speed_test
from core.config import BASE_URL


class FreeTimesRepository:

    @speed_test
    async def get_free_dates_for_doctor(
            self,
            filial_id,
            filial_cash_id,
            department_id,
            doctor_id,
            start=None,
            end=None
    ) -> List[str]:
        if start is None and end is None:
            start, end = self._get_month_interval()
        elif start is None:
            start, _ = self._get_month_interval()
        elif end is None:
            _, end = self._get_month_interval()
        data = await self._get_data_for_doctor(filial_id, filial_cash_id, department_id, doctor_id, start, end)

        free_dates = [times["workDate"] for times in data["intervals"] if times["isFree"]]
        free_dates.append("20211224")
        return free_dates

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

    async def _get_data_for_doctor(self, filial_id, filial_cash_id, department_id, doctor_id, start, end):
        url = f"{BASE_URL}api/reservation/schedule?st={start}&en={end}&doctor={doctor_id}&filialId={filial_id}&cashlist={filial_cash_id}&speclist={department_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        return response.json()["data"][0]

    async def get_free_times_for_doctor(self, filial_id, filial_cash_id, department_id, doctor_id, free_date) -> List[str]:
        url = f"{BASE_URL}api/reservation/intervals?st={free_date}&en={free_date}&spec={department_id}&dcode={doctor_id}&filialId={filial_id}&cashlist={filial_cash_id}&inFilials={filial_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        return self._get_free_times(response.json()["data"])

    def _get_free_times(self, dates):
        free_dates = []
        for i in range(0, len(dates)):
            date = dates[i]["workdates"][0]
            for key, value in date.items():
                free_dates += [interval["time"] for interval in value[0]["intervals"] if not interval["isFree"]]

        return free_dates

