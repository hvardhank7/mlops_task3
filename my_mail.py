#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("tarungarg20001@gmail.com", "Darpan786") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("tarungarg20001@gmail.com", "hvardhank7@gmail.com", message) 
# terminating the session 
s.quit()


# In[ ]:




