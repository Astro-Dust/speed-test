import speedtest
import os

def speed_test():
    st = speedtest.Speedtest()
    download_speed_bps = st.download()
    upload_speed_bps = st.upload()
    ping = st.results.ping

    # convertendo para Mbps (10)
    download_speed_mbps = download_speed_bps / 10 ** 5
    upload_speed_mbps = upload_speed_bps / 10 ** 5

    print(f'Download speed: {download_speed_mbps:.2f} Mbps')
    print(f'Upload speed: {upload_speed_mbps:.2f} Mbps')
    print(f'Ping: {ping} ms')

if __name__ == '__main__':
    os.system('cls || clear')
    print('Testing internet speed...')
    speed_test()