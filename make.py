from PIL import Image, ImageDraw

images = []

for i in range(51):
    image = Image.open('./image/fake_samples_epoch_%03d.png' % (i*50))
    images.append(image)

#image.save(保存場所, 全ての画像を保存, 追加の画像, 未使用の色の圧縮をしない, 各画像の表示時間, 無限ループ)
images[0].save('./train_process.gif', \ 
                save_all=True, \
                append_images=images[1:], \
                optimizer=False, \
                duration=750, \
                loop=0)