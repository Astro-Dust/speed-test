import speedtest
import os
import matplotlib.pyplot as plt

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

    # criação do gráfico
    labels = ['Download', 'Upload', 'Ping']
    values = [download_speed_mbps, upload_speed_mbps, ping]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'green', 'red'])
    plt.xlabel('Measurement')
    plt.ylabel('Value')
    plt.title('Internet Speed')
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    os.system('cls || clear')
    print('Testing internet speed...')
    speed_test()