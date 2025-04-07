import os
import json
import shutil

files = {
    
    "E03_C009_008_0.wav": "E03_C009_008_1.wav",
	"E08_C000_212_0.wav": "E08_C000_212_1.wav",
	"E08_C003_070_0.wav": "E08_C003_070_1.wav",
	"E08_C006_190_0.wav": "E08_C006_190_1.wav",
	"E08_C013_353_0.wav": "E08_C013_353_1.wav",
	"E08_C016_046_0.wav": "E08_C016_046_1.wav",
	"E09_C001_154_0.wav": "E09_C001_154_1.wav",
	"E10_C004_361_0.wav": "E10_C004_361_1.wav",
	"E11_C005_020_0.wav": "E11_C005_020_1.wav",
	"E11_C005_407_0.wav": "E11_C005_407_1.wav",
	"E11_C022_476_0.wav": "E11_C022_476_1.wav",
	"E12_C003_356_0.wav": "E12_C003_356_1.wav",
	"E14_C000_247_0.wav": "E14_C000_247_1.wav",
	"E14_C003_200_0.wav": "E14_C003_200_1.wav",
	"E14_C013_364_0.wav": "E14_C013_364_1.wav",
    
	"A09_C003_194_0.wav": "A09_C003_194_1.wav",
	"A10_C002_109_0.wav": "A10_C002_109_1.wav",
	"A03_C009_135_0.wav": "A03_C009_135_1.wav",
	"A09_C001_036_0.wav": "A09_C001_036_1.wav",
	"A00_C007_558_0.wav": "A00_C007_558_1.wav",
	"A00_C007_1111_0.wav": "A00_C007_1111_1.wav",
	"A01_C013_167_0.wav": "A01_C013_167_1.wav",
	"A03_C000_044_0.wav": "A03_C000_044_1.wav",
	"A10_C010_164_0.wav": "A10_C010_164_1.wav",
	"A04_C000_235_0.wav": "A04_C000_235_1.wav",
	"A04_C000_136_0.wav": "A04_C000_136_1.wav",
	"A02_C003_774_0.wav": "A02_C003_774_1.wav",
	"A00_C001_133_0.wav": "A00_C001_133_1.wav",
	"A07_C003_385_0.wav": "A07_C003_385_1.wav",
	"A01_C007_071_0.wav": "A01_C007_071_1.wav",
}

data_dir = '/home/lam/Downloads/vits2_pytorch/fonos_voice_v1/wavs/'
map_data = {}
new_files = {}
gt_dir = './audios/GT/'
gen_dir = './audios/scratch/'
data = {}

with open("./metadata.csv", 'r') as f:
	for line in f.readlines():
		file_name = line.split('|')[0].split('/')[-1]
		if file_name.replace('.wav', '_0.wav') in files:
			new_GT = file_name.replace('.wav', '_0.wav')
			shutil.copy(data_dir + file_name, gt_dir + new_GT)
			data[new_GT] = line.split('|')[-1]

with open('./audios/file_text.json', 'w') as fo:       
	json.dump(data, fo, indent=4, ensure_ascii=False)
        
print(data)