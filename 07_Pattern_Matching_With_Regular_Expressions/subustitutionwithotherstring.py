import re
agentname=re.compile(r'Agent (\w)\w*')
om=agentname.sub(r'\1****','Agent Alace told Agent Carol that Agent Eve knew Bob wa a double Agent')
