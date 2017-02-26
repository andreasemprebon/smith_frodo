import subprocess
import json
from lxml import etree

###
# Il comando e':
# ﻿java -cp frodo2.jar frodo2.algorithms.AgentFactory smith.xcsp DPOPagentJaCoP_SMITh.xml
###

time_steps = 30

frodo = subprocess.run(["java", "-cp", "frodo2.jar", "frodo2.algorithms.AgentFactory",
                        "smith.xcsp", "DPOPagentJaCoP_SMITh.xml"], stdout=subprocess.PIPE)

output   = frodo.stdout
bindings = {}
results  = {}
for line in output.splitlines():
    text = str(line).replace("b\"", "").replace("\"", "")
    if text.startswith("var"):
        equal_pos = text.index("=")
        name  = text[5:equal_pos-2]
        value = int( text[equal_pos+2:] )
        bindings[name] = value

#print(bindings)

xcsp            = etree.parse("smith.xcsp")
xcsp_variables  = xcsp.find("variables")
xcsp_agents     = xcsp.find("agents")

for agent in xcsp_agents.findall("agent"):
    name = agent.get("name")
    results[name] = [ 0 ] * time_steps

for var in xcsp_variables.findall("variable"):
    name    = var.get("name")
    agent   = var.get("agent")

    index = int( name[-1:] )

    results[ agent ][index] = bindings[name]

print(results)

with open('data.json', 'w') as outfile:
    json.dump(results, outfile)