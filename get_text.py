import metrohash
import os

h = metrohash.MetroHash128()

files = {
    
    "DuyenFPT_1293.wav": "DuyenFPT_1293_eval.wav",
	"DuyenFPT_1476.wav": "DuyenFPT_1476_eval.wav",
	"DuyenFPT_1935.wav": "DuyenFPT_1935_eval.wav",
	"DuyenFPT_2144.wav": "DuyenFPT_2144_eval.wav",
	"DuyenFPT_3503.wav": "DuyenFPT_3503_eval.wav",
	"DuyenFPT_3681.wav": "DuyenFPT_3681_eval.wav",
	"DuyenFPT_4109.wav": "DuyenFPT_4109_eval.wav",
	"DuyenFPT_4446.wav": "DuyenFPT_4446_eval.wav",
	"DuyenFPT_4543.wav": "DuyenFPT_4543_eval.wav",
	"DuyenFPT_5642.wav": "DuyenFPT_5642_eval.wav",
	"DuyenFPT_5734.wav": "DuyenFPT_5734_eval.wav",
	"DuyenFPT_5850.wav": "DuyenFPT_5850_eval.wav",
	"DuyenFPT_5968.wav": "DuyenFPT_5968_eval.wav",
	"DuyenFPT_6219.wav": "DuyenFPT_6219_eval.wav",
	"DuyenFPT_6498.wav": "DuyenFPT_6498_eval.wav",
	"DuyenFPT_6626.wav": "DuyenFPT_6626_eval.wav",
	"DuyenFPT_7387.wav": "DuyenFPT_7387_eval.wav",
	"DuyenFPT_8731.wav": "DuyenFPT_8731_eval.wav",
	"DuyenFPT_8849.wav": "DuyenFPT_8849_eval.wav",
	"DuyenFPT_9038.wav": "DuyenFPT_9038_eval.wav",
	"DuyenFPT_9695.wav": "DuyenFPT_9695_eval.wav",
}
map_data = {}
new_files = {}
gt_dir = './audios/GT/'
gen_dir = './audios/scratch/'
with open('./audios/file_text.json', 'w') as fo:
    with open("/home/lam/TTS/Data/FPT-Speech-1.0/metadata_phoneme.txt", 'r') as f:
        for line in f.readlines():
            if line.split('|')[0] + '.wav' in files:
                h.update(bytes(line.split('|')[0], 'utf-8'))
                new_GT = h.hexdigest()+'.wav'
                h.update(bytes(line.split('|')[0]+'_eval', 'utf-8'))
                new_eval = h.hexdigest()+'.wav'
                new_files[new_GT] = new_eval
                # os.rename(gt_dir + line.split('|')[0] + '.wav', gt_dir + new_GT)
                os.rename(gen_dir + line.split('|')[0] + '_eval.wav', gen_dir + new_eval)
                print('\"' + new_GT + '\": ' + '\"'+line.split('|')[-1][:-1] + '\",')
print(new_files)