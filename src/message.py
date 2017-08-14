import smtplib
import config as cfg


def send_message(msg, sender, recipients):
    conn = smtplib.SMTP_SSL(cfg.SMTPserver, cfg.SMTPport)
    conn.ehlo()
    conn.login(cfg.USERNAME, cfg.PASSWORD)
    conn.sendmail(sender, recipients, msg)
    conn.quit()
