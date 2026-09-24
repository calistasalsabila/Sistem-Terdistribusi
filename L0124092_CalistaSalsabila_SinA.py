from datetime import datetime, timedelta

master_time = datetime.now()

nodes = {
    "Node 1": master_time + timedelta(seconds=-5),
    "Node 2": master_time + timedelta(seconds=7),
    "Node 3": master_time + timedelta(seconds=3),
    "Node 4": master_time + timedelta(seconds=-2)
}


print("BERKELEY CLOCK SYNCHRONIZATION\n")

# Menampilkan waktu awal
print("Waktu awal:")
print(f"Master  : {master_time.strftime('%H:%M:%S')}")

for name, time in nodes.items():
    print(f"{name:<8}: {time.strftime('%H:%M:%S')}")


# Menghitung offset setiap node terhadap master
offsets = {}

for name, time in nodes.items():
    offset = (time - master_time).total_seconds()
    offsets[name] = offset


# Menghitung rata-rata offset
total_offset = sum(offsets.values())
average_offset = total_offset / (len(offsets) + 1)


print("\nOffset terhadap Master:")

print(f"Master  : {0:+.0f} detik")

for name, offset in offsets.items():
    print(f"{name:<8}: {offset:+.0f} detik")


print(f"\nRata-rata offset: {average_offset:+.2f} detik")


# Menghitung waktu setelah sinkronisasi
synchronized_master = master_time + timedelta(seconds=average_offset)

synchronized_nodes = {}

for name, time in nodes.items():
    synchronized_nodes[name] = time + timedelta(
        seconds=(average_offset - offsets[name])
    )


# Menampilkan hasil sinkronisasi
print("\nHASIL SINKRONISASI")

print(
    f"Master  : "
    f"{synchronized_master.strftime('%H:%M:%S.%f')[:-3]}"
)

for name, time in synchronized_nodes.items():
    print(
        f"{name:<8}: "
        f"{time.strftime('%H:%M:%S.%f')[:-3]}"
    )