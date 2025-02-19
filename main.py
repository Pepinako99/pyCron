from crontab import CronTab

# Crear objeto crontab para el usuario actual
cron = CronTab(user=True)

# Crear nueva tarea
job = cron.new(command='python3 /home/user/miscript.py')

# Configurar para que se ejecute cada minuto
job.minute.every(1)

# Guardar cambios
cron.write()

print("Tarea programada con éxito.")
