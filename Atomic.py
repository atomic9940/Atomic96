import os
from os import system as ss
import random
ll = 'pip install'
try:
	from cfonts import render
except ModuleNotFoundError:
	ss(ll+' python-cfonts')
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout
)
from aiohttp_socks import ProxyConnector
from fake_useragent import FakeUserAgent
from datetime import datetime
from colorama import *
import asyncio, time, json, os, pytz
wib = pytz.timezone('Asia/Jakarta')

print(f'''{render('Script', colors=['red', 'yellow'], align='center')}''')
print(f'''{render('Atomic', colors=['green', 'yellow'], align='center')}''')
print("""\033[1;37m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                    
║\33[0;41m[ ENTER THE TOOL'S PASSWORD ✅ ] \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝              """)
password ='Atomic996'
one = str(input('''❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 :  ''') )
if one == password:
    print(f"""
𝐘𝐨𝐮 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐥𝐨𝐠𝐠𝐞𝐝 𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥 ⚡ """)
    time.sleep(1)
else:
    exit("""
𝚃𝚑𝚎 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝚒𝚜 𝚒𝚗𝚌𝚘𝚛𝚛𝚎𝚌𝚝 ❌ 
𝙿𝚕𝚎𝚊𝚜𝚎 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 𝚝𝚑𝚎 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚝𝚘 𝚏𝚒𝚗𝚍 𝚘𝚞𝚝 @Atomic994 ✅""")

time.sleep(3)
os.system('clear') 

print(f"""
{render('solix', colors=['green', 'yellow'], align='center')}
{render('Atomic', colors=['green', 'yellow'], align='center')}
\033[1;37m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                    
║\33[0;41m[Search for my channel On Telegram : Airdrop_web3_ato ]\033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝              
\033[1;37m
\33[0;41m Auto Task & Auto Play ✅ \033[0;92m 
\033[1;37m
\33[0;42m Developer : @Atomic994 ☠️ \033[0;92m
\033[1;37m
\33[0;43m  Developer channel : https://t.me/Airdrop_web3_ato 👻 \033[0;92m """)


class Solix:
    def __init__(self) -> None:
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Origin": "chrome-extension://ocanmekhhffgpiiambnjmlconhhfgolg",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Storage-Access": "active"
        }
        self.BASE_API = "https://api.solixdepin.net/api"
        self.ref_code = "99DqVgWH" # U can change it with yours.
        self.proxies = []
        self.proxy_index = 0
        self.account_proxies = {}
        self.access_tokens = {}
        self.refresh_tokens = {}
        self.request_counter ={}

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Ping {Fore.BLUE + Style.BRIGHT}Solix - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT} Telegram Channel link :{Fore.YELLOW + Style.BRIGHT} https://t.me/Airdrop_web3_ato
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_accounts(self):
        filename = "accounts.json"
        try:
            if not os.path.exists(filename):
                self.log(f"{Fore.RED}File {filename} Not Found.{Style.RESET_ALL}")
                return

            with open(filename, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                return []
        except json.JSONDecodeError:
            return []
            
     async def human_delay(self, min=45, max=135):
            """تأخير عشوائي  مع ارتجاج لمحكات السلوك البشري """
            delay = random.uniform(min, max) + random.uniform(-1, 59)
            await asyncio.sleep(max(0.5, delay))
    
    async def rotate_user_agent(self):
        """تغيير User-Agent عشوائياً لكل طلب"""
        self.headers["User-Agent"] = FakeUserAgent().random
            
    async def load_proxies(self, use_proxy_choice: int):
        filename = "proxy.txt"
        try:
            if use_proxy_choice == 1:
                async with ClientSession(timeout=ClientTimeout(total=30)) as session:
                    async with session.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt") as response:
                        response.raise_for_status()
                        content = await response.text()
                        with open(filename, 'w') as f:
                            f.write(content)
                        self.proxies = content.splitlines()
                        random.shuffle(self.proxies)
            else:
                if not os.path.exists(filename):
                    self.log(f"{Fore.RED + Style.BRIGHT}File {filename} Not Found.{Style.RESET_ALL}")
                    return
                with open(filename, 'r') as f:
                    self.proxies = f.read().splitlines()
                    random.shuffle(self.proxies)
            
            if not self.proxies:
                self.log(f"{Fore.RED + Style.BRIGHT}No Proxies Found.{Style.RESET_ALL}")
                return

            self.log(
                f"{Fore.GREEN + Style.BRIGHT}Proxies Total  : {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(self.proxies)}{Style.RESET_ALL}"
            )
        
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}Failed To Load Proxies: {e}{Style.RESET_ALL}")
            self.proxies = []
            
     async def rate_limit_check(self, email):
        """التحكم في معدل الطلبات لكل حساب"""
        if email not in self.request_counter:
            self.request_counter[email] = {
                'count': 0,
                'last_reset': time.time()
            }
        
        now = time.time()
        if now - self.request_counter[email]['last_reset'] > 3600:  # إعادة الضبط كل ساعة
            self.request_counter[email] = {
                'count': 0,
                'last_reset': now
            }
        
        self.request_counter[email]['count'] += 1
        if self.request_counter[email]['count'] > 50:  # الحد الأقصى 50 طلب/ساعة
            await asyncio.sleep(random.uniform(30, 120))  # تأخير طويل إذا تجاوز الحد

    async def auth_login(self, email: str, password: str, proxy=None, retries=5):
        await self.rate_limit_check(email)
        await self.rotate_user_agent()
        await self.human_delay()
        
        url = f"{self.BASE_API}/auth/login-password"
        data = json.dumps({"email":email,"referralByCode":self.ref_code,"captchaToken":"","password":password})
        headers = {
            **self.headers,
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }

    def check_proxy_schemes(self, proxies):
        schemes = ["http://", "https://", "socks4://", "socks5://"]
        if any(proxies.startswith(scheme) for scheme in schemes):
            return proxies
        return f"http://{proxies}"

    def get_next_proxy_for_account(self, token):
        if token not in self.account_proxies:
            if not self.proxies:
                return None
            proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
            self.account_proxies[token] = proxy
            self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return self.account_proxies[token]

    def rotate_proxy_for_account(self, token):
        if not self.proxies:
            return None
        proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
        self.account_proxies[token] = proxy
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return proxy
    
    def mask_account(self, account):
        if "@" in account:
            local, domain = account.split('@', 1)
            mask_account = local[:3] + '*' * 3 + local[-3:]
            return f"{mask_account}@{domain}"

    def print_message(self, account, proxy, color, message):
        self.log(
            f"{Fore.CYAN + Style.BRIGHT}[ Account:{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} {account} {Style.RESET_ALL}"
            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
            f"{Fore.CYAN + Style.BRIGHT} Proxy: {Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
            f"{Fore.MAGENTA + Style.BRIGHT} - {Style.RESET_ALL}"
            f"{Fore.CYAN + Style.BRIGHT}Status:{Style.RESET_ALL}"
            f"{color + Style.BRIGHT} {message} {Style.RESET_ALL}"
            f"{Fore.CYAN + Style.BRIGHT}]{Style.RESET_ALL}"
        )

    def print_question(self):
        while True:
            try:
                print("1. Run With Monosans Proxy")
                print("2. Run With Private Proxy")
                print("3. Run Without Proxy")
                choose = int(input("Choose [1/2/3] -> ").strip())

                if choose in [1, 2, 3]:
                    proxy_type = (
                        "Run With Monosans Proxy" if choose == 1 else 
                        "Run With Private Proxy" if choose == 2 else 
                        "Run Without Proxy"
                    )
                    print(f"{Fore.GREEN + Style.BRIGHT}{proxy_type} Selected.{Style.RESET_ALL}")
                    return choose
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Please enter either 1, 2 or 3.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}Invalid input. Enter a number (1, 2 or 3).{Style.RESET_ALL}")

    async def auth_login(self, email: str, password: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/auth/login-password"
        data = json.dumps({"email":email,"referralByCode":self.ref_code,"captchaToken":"","password":password})
        headers = {
            **self.headers,
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result["data"]
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"GET Auth Token Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def auth_refresh(self, email: str, password: str, use_proxy: bool, proxy=None, retries=5):
        await self.rate_limit_check(email)
        await self.rotate_user_agent()
        await self.human_delay()
        url = f"{self.BASE_API}/auth/refresh"
        data = json.dumps({"refreshToken":self.refresh_tokens[email]})
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.refresh_tokens[email]}",
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        if response.status == 401:
                            await self.process_user_login(email, password, use_proxy)
                            data = json.dumps({"refreshToken":self.refresh_tokens[email]})
                            headers["Authorization"] = f"Bearer {self.refresh_tokens[email]}"
                            continue
                        response.raise_for_status()
                        result = await response.json()
                        return result["data"]
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"Refreshing Auth Token Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def get_total_point(self, email: str, proxy=None, retries=5):
        await self.rate_limit_check(email)
        await self.rotate_user_agent()
        await self.human_delay(3, 7)
        url = f"{self.BASE_API}/point/get-total-point"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result["data"]
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"GET Earning Data Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def get_connection_quality(self, email: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/point/get-connection-quality"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}"

        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        result = await response.text()
                        return json.loads(result)
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"GET Connection Quality Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def get_user_task(self, email: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/task/get-user-task"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        result = await response.text()
                        return json.loads(result)
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"GET Task Lists Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def perform_task(self, email: str, task_id: str, title: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/task/do-task"
        data = json.dumps({"taskId":task_id})
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}",
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"Perform Task {title} Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def claim_task(self, email: str, task_id: str, title: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/task/claim-task"
        data = json.dumps({"taskId":task_id})
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}",
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"Task {title} Not Claimed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def start_earn_point(self, email: str, proxy=None, retries=5):
        url = f"{self.BASE_API}/point/start-earn-point"
        headers = {
            **self.headers,
            "Authorization": f"Bearer {self.access_tokens[email]}",
            "Content-Length": "0"
        }
        for attempt in range(retries):
            connector = ProxyConnector.from_url(proxy) if proxy else None
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.text()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                return self.print_message(self.mask_account(email), proxy, Fore.RED, f"Start Node Failed: {Fore.YELLOW+Style.BRIGHT}{str(e)}")
    
    async def process_user_login(self, email: str, password: str, use_proxy: bool):
        proxy = self.get_next_proxy_for_account(email) if use_proxy else None
        token = None
        while token is None:
            token = await self.auth_login(email, password, proxy)
            if not token:
                proxy = self.rotate_proxy_for_account(email) if use_proxy else None
                await asyncio.sleep(5)
                continue

            self.access_tokens[email] = token["accessToken"]
            self.refresh_tokens[email] = token["refreshToken"]
            self.print_message(self.mask_account(email), proxy, Fore.GREEN, "GET Auth Token Success")
            await self.process_start_earn_point(email, use_proxy)
            return self.access_tokens[email], self.refresh_tokens[email]
        
    async def process_refreshing_token(self, email: str, password: str, use_proxy: bool):
        while True:
            await asyncio.sleep(55 * 60)   

            proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            token = None
            while token is None:
                token = await self.auth_refresh(email, password, use_proxy, proxy)
                if not token:
                    proxy = self.rotate_proxy_for_account(email) if use_proxy else None
                    await asyncio.sleep(5)
                    continue

                self.access_tokens[email] = token["accessToken"]
                self.refresh_tokens[email] = token["refreshToken"]
                self.print_message(self.mask_account(email), proxy, Fore.GREEN, "Refreshing Auth Token Success")     
        
    async def process_start_earn_point(self, email: str, use_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            
            start = await self.start_earn_point(email, proxy)
            if start and start.strip() == "true":
                self.print_message(self.mask_account(email), proxy, Fore.GREEN, "Start Node Success")
                return True
            else:
                self.print_message(self.mask_account(email), proxy, Fore.RED, "Start Node Failed")
                await asyncio.sleep(5)
                continue   
        
    async def process_get_total_point(self, email: str, use_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            display = "N/A PTS"

            earning = await self.get_total_point(email, proxy)
            if earning:
                point_total = earning.get("total", 0)
                display = f"{point_total:.0f} PTS"

            self.print_message(self.mask_account(email), proxy, Fore.BLUE, "Earining: "
                f"{Fore.WHITE+Style.BRIGHT}{display}{Style.RESET_ALL}"
            )

            await asyncio.sleep(10 * 60)        
        
    async def process_get_connection_quality(self, email: str, use_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None
            quality = "N/A"

            connection = await self.get_connection_quality(email, proxy)
            if connection:
                quality = connection.get("data")

            self.print_message(self.mask_account(email), proxy, Fore.BLUE, "Connection Quality: "
                f"{Fore.WHITE+Style.BRIGHT}{quality}{Style.RESET_ALL}"
            )

            await asyncio.sleep(20)     
        
    async def process_completing_user_task(self, email: str, use_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(email) if use_proxy else None

            task_lists = await self.get_user_task(email, proxy)
            if task_lists:
                tasks = task_lists.get("data", [])

                completed = False
                for task in tasks:
                    if task:
                        task_id = task.get("_id")
                        title = task.get("name")
                        reward = task.get("pointAmount")
                        status = task.get("status")

                        if status == "idle":
                            perform = await self.perform_task(email, task_id, title, proxy)
                            if perform and perform.get("result") == "success":
                                self.print_message(self.mask_account(email), proxy, Fore.WHITE, 
                                    f"Perform Task {title} "
                                    f"{Fore.GREEN+Style.BRIGHT}Success{Style.RESET_ALL}"
                                )

                                claim = await self.claim_task(email, task_id, title, proxy)
                                if claim and claim.get("result") == "success":
                                    self.print_message(self.mask_account(email), proxy, Fore.WHITE, 
                                        f"Task {title}"
                                        f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.CYAN+Style.BRIGHT} Reward: {Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT}{reward} PTS{Style.RESET_ALL}"
                                    )

                        elif status == "pending":
                            claim = await self.claim_task(email, task_id, title, proxy)
                            if claim and claim.get("result") == "success":
                                self.print_message(self.mask_account(email), proxy, Fore.WHITE, 
                                    f"Task {title}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.CYAN+Style.BRIGHT} Reward: {Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT}{reward} PTS{Style.RESET_ALL}"
                                )
                        else:
                            completed = True

                if completed:
                    self.print_message(self.mask_account(email), proxy, Fore.GREEN, "All Available Tasks Is Completed")

            await asyncio.sleep(24 * 60 * 60)     
        
    async def process_accounts(self, email: str, password: str, use_proxy: bool):
        # تأخير عشوائي قبل بدء كل حساب
        await asyncio.sleep(random.uniform(5, 30))
        
        self.access_tokens[email], self.refresh_tokens[email] = await self.process_user_login(email, password, use_proxy)
        if self.access_tokens[email] and self.refresh_tokens[email]:
            tasks = [
                asyncio.create_task(self.process_refreshing_token(email, password, use_proxy)),
                asyncio.create_task(self.process_get_total_point(email, use_proxy)),
                asyncio.create_task(self.process_get_connection_quality(email, use_proxy)),
                asyncio.create_task(self.process_completing_user_task(email, use_proxy))
            ]
            await asyncio.gather(*tasks)

    async def main(self):
        try:
            accounts = self.load_accounts()
            if not accounts:
                self.log(f"{Fore.RED+Style.BRIGHT}No Accounts Loaded.{Style.RESET_ALL}")
                return
            
            use_proxy_choice = self.print_question()

            use_proxy = False
            if use_proxy_choice in [1, 2]:
                use_proxy = True

            self.clear_terminal()
            self.welcome()
            self.log(
                f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT}{len(accounts)}{Style.RESET_ALL}"
            )

            if use_proxy:
                await self.load_proxies(use_proxy_choice)

            self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

            while True:
                tasks = []
                for account in accounts:
                    email = account.get('Email')
                    password = account.get('Password')

                    if "@" in email and password:
                        tasks.append(asyncio.create_task(self.process_accounts(email, password, use_proxy)))
                        await asyncio.sleep(random.uniform(30, 120))  # تأخير بين إنشاء المهام

                await asyncio.gather(*tasks)
                await asyncio.sleep(random.uniform(60, 240))  # تأخير عشوائي بين الدورات

        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")
            raise e

if __name__ == "__main__":
    try:
        bot = Solix()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Solix - BOT{Style.RESET_ALL}                                       "                              
)
