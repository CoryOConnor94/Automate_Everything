import cv2

elf_image = cv2.imread('elfs.jpeg')
watermark = cv2.imread('watermark.png')

print(watermark.shape)
x = elf_image.shape[1] - watermark.shape[1]
y = elf_image.shape[0] - watermark.shape[0]

watermark_place = elf_image[y:, x:]
cv2.imwrite('watermark_place.jpeg', watermark_place)

blend =cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
cv2.imwrite('blend.jpeg', blend)

elf_image[y:, x:] = blend
cv2.imwrite('elfs-watermarked.jpeg', elf_image)