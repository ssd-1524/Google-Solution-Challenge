from django.shortcuts import render
from .models import Parking
import subprocess
import time
# Create your views here.


def table_view(request):
    def run_command(command):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def run_command_repeatedly(command, interval_minutes=1):
        while True:
            run_command(command)
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds

    if __name__ == "__main__":
        # Replace the command below with the command you want to run
        your_command = "python -c 'from csvFile.resources import import_data_from_csv\nimport_data_from_csv(\"C:/Users/yansh/OneDrive/Desktop/output.csv\")'"
        run_command_repeatedly(your_command)

    obj = Parking.objects.all()
    return render(request, 'table.html', {
        'obj_lst': obj,
    })
