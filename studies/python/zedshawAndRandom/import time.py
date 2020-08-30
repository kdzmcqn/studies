import time
import html
time.sleep(10) #no. of seconds to sleep
# NameOfModule.FunctionToInvoke

time.strftime("%H:%M") #hour : minute

time.strftime("%A %p") #day of the week and AM/PM

# detect and remove tags
html.escape("This HTML fragment contains a <script>script</script> tag.")

# encoded html return tp original form
html.unescape("I &hearts: Python's standard library&gt:.")