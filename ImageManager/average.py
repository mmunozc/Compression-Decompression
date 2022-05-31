
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv("compression_benchmarks_ImS.csv")
df = pd.read_csv("decompression_benchmarks_ImS.csv")

#df = pd.read_csv("compression_benchmarks_RunLength.csv")
#df = pd.read_csv("decompression_benchmarks_RunLength.csv")



avgTime = df["time"].mean()
avgMemory = df["memory"].mean()
avgFileSize = df["filesize"].mean()

print("average_time:", avgTime, "// avergae_memory: ", avgMemory, "// average_file size: ", avgFileSize)


df = df.sort_values(by=["filesize"])

_, ax = plt.subplots()
ax.scatter(df["filesize"], df["time"], color="#069A55")
ax.set_title("Time Consumption")
ax.set_xlabel('Image Size (MB)', labelpad=30,
                      rotation=90)  # set x axis label
ax.set_ylabel('Time Consumption (s)', labelpad=30,
                      rotation=90)  # set y axis label
# ax.legend(loc="upper left", bbox_to_anchor=(0.08, 1),
#                   fancybox=True, shadow=True, ncol=1) 
plt.tight_layout()
#plt.savefig("time(Compressio_ImageScalling).png")
plt.savefig("time(Decompressio_ImageScalling).png")

#plt.savefig("time(Compressio_RunLength).png")
#plt.savefig("time(Decompressio_RunLength).png")


_, ax = plt.subplots()
ax.scatter(df["filesize"], df["memory"], color="#0A5569")
ax.set_title("Memory Consumption")
ax.set_xlabel('Image Size (MB)', labelpad=30,
                      rotation=90)  # set x axis label
ax.set_ylabel('Memory Consumption (mb)', labelpad=30,
                      rotation=90)  # set y axis label
# ax.legend(loc="upper left", bbox_to_anchor=(0.08, 1),
#                   fancybox=True, shadow=True, ncol=1) 
plt.tight_layout()
# plt.show()
#plt.savefig("space(Compressio_ImageScalling).png")
plt.savefig("space(Decompressio_ImageScalling).png")

#plt.savefig("space(Compressio_RunLength).png")
#plt.savefig("space(Decompressio_RunLength).png")

