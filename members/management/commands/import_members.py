from django.core.management.base import BaseCommand
from members.models import Member
import pandas as pd


class Command(BaseCommand):
    help = "Import members from Excel file"

    def handle(self, *args, **kwargs):

        file_path = "members.xlsx"

        df = pd.read_excel(file_path)

        imported = 0
        skipped = 0

        for _, row in df.iterrows():

            member_number = str(row.get("Member Number", "")).strip()

            if not member_number:
                continue

            if Member.objects.filter(member_number=member_number).exists():
                skipped += 1
                continue

            Member.objects.create(
                member_number=member_number,
                full_name=str(row.get("Member Name", "")).strip(),
                phone_number=str(row.get("Primary Phone", "")).strip(),
                gender=str(row.get("Gender", "")).strip()[:1].upper(),
                address=str(
                    row.get(
                        "Estate/Town/Physical Address",
                        ""
                    )
                ).strip(),
            )

            imported += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Imported: {imported} | Skipped: {skipped}"
            )
        )