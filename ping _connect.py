import os, argparse, requests, json

#сканнер через командное окно
def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    response = os.popen(f'ping -n 1 {scanned_ip}') 
    res = response.readlines()
    return f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}"

def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()
    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        try:
            response = requests.get(target, headers=headers_dict, timeout=10)
        except requests.exceptions.Timeout:
            return f"Время ожидания ответа {target} вышло\n"
        except:
            return f"Неверный адрес ресурса {target}\n"
    elif method == "POST":
        try:
            response = requests.post(target, headers=headers_dict, data=payload, timeout=10)
        except requests.exceptions.Timeout:
            return f"Время ожидания ответа {target} вышло\n"
    else:
        return f"Не выбран метод GET или POST для ресурса {target}\n"
    response.close()
    return(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}")


post_request_payload = None
parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
parser.add_argument('-t', '--target', type=str, help='address')
parser.add_argument('-i', '--ip', type=str, help='IP address')
parser.add_argument('-n', '--num_of_hosts',type=int, help='Number of hosts')
parser.add_argument('-m', '--method',choices=['GET', 'POST'], type=str, help='GET/POST')
parser.add_argument('-hd', '--headers',type=str, help='headers', nargs='*')
parser.add_argument('-p', '--payload',type=str, help='POST request payload')
args = parser.parse_args()
if args.task == 'scan':
    for host_num in range(args.num_of_hosts): 
        print(do_ping_sweep(args.ip , host_num))
if args.task == 'sendhttp':
    print(sent_http_request(args.target, args.method, args.headers, args.payload))
