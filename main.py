from send_mail import send_mail

routes = ('//cloud-data2/Backup', '//cl-cloud-sto1/cloud/Backup', '//cl-cloud-sto2/Cloud/Backup', '//CL-CLOUD-STO4/Cloud/Backup')
mails = ["<email@email.com>"]
subject = 'Estatus Diario Backup CCC Claro ✔'

send_mail(routes, mails, subject)