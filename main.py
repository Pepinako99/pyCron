from crontab import CronTab

# Crear objeto crontab para el usuario actual
cron = CronTab(user=True)

# Crear nueva tarea
job = cron.new(command='export DISPLAY=0 && export XDG_RUNTIME_DIR=/rum/user/1000 && dunstify -u citical --icon="info" --appname="Nombre del proceso" "Titulo" "Mensaje"')

# Configurar para que se ejecute cada minuto
job.minute.on(50)

job.hour.on(18)
job.day.on(19)
job.month.on(2)

# Guardar cambios
cron.write()

print("Tarea programada con éxito.")
