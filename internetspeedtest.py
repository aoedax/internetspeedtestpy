#pip install speedtest-cli

import speedtest

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers() # -> get list of servers
print("Choosing best server...")
best = test.get_best_server() # -> choost best server
print(f"FoundL {best['host']} located in {best['country']}")

print("Performing download test...")
download_result = test.download()
print("Performing upload test...")
upload_result = test.upload()
ping_result = test.results.ping

print("----------Test Results----------")
print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f}ms")
print("--------------------------------")