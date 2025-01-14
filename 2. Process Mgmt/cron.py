import os

script="my_file.py"
with open(script, "w") as file:
    file.write("""
import os
os.system('echo "Hello World" ')
""")
new_cron=f"* * * * * python3 {script}"
os.popen("crontab -l").read() +new_cron
cron_dir='/var/spool/cron/crontabs/ali'

# run ->operational excelllence
# safely -> security
# recover->reliablility
# perform -> performance efficeincy
# save->cost optimization
# green->sustainability

# Set the new crontab
with open(cron_dir, 'w') as cron_file:
    cron_file.write(new_cron)  # Write to a temporary file
os.system(f'crontab {cron_dir}')  # Load the new crontab

# Optional: Print a message and exit gracefully
print(f"Cron job added: {new_cron}")
# *->min
# *->hr
# *->day of the month
# *->month
# *-> day of the week
