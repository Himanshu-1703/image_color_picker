import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
from sklearn.cluster import MiniBatchKMeans

# path of the image file
image = 'notebooks\stats.jpeg'

# function to read the image
def read_img(image):
    img_arr = plt.imread(image)
    return img_arr

# function to resize the image as 2D array
def resize_image(image):
    X = image.reshape(-1,3)
    return X

# fit the kmeans model and get the cluster centroids
def get_cluster_centroids(colors,image_array):
    kmeans = MiniBatchKMeans(n_clusters=colors,init='k-means++',init_size=10)
    # fit the KMeans model
    kmeans.fit(image_array)
    # get the cluster centroid co-ordinates
    cluster_centroids = kmeans.cluster_centers_
    return cluster_centroids

# make the color palette
def make_color_palette(n_clusters,cluster_centers,palette_size=(450,100)):
    # create a new image object
    palette = Image.new(mode='RGB',size=palette_size)
    # draw object to draw on newly created image
    draw_palette = ImageDraw.Draw(im=palette,mode='RGB')
    
    # color input is taken as integers
    cluster_centers = cluster_centers.astype('int')
    
    swatch_width = palette_size[0] / cluster_centers.shape[0]
    
    # draw each color swatch in loop
    for i,color in enumerate(cluster_centers):
        draw_palette.rectangle([(i*swatch_width,0),((i+1)*swatch_width,palette_size[1])],fill=tuple(color))
        
    return palette


def main(image,n_clusters):
    # read the image
    img = read_img(image)
    
    if img.ndim == 3:
        
        # resize image
        image_array = resize_image(img)

        # run kmeans
        centroids = get_cluster_centroids(n_clusters,image_array=image_array)

        palette_size = (n_clusters*150,100)

        # make the image
        color_palette = make_color_palette(n_clusters=n_clusters,
                                            cluster_centers=centroids,
                                            palette_size=palette_size)

        return color_palette
        

if __name__ == '__main__':
    color_palette = main(image=image,n_clusters=5)
    
    plt.imshow(color_palette)
    plt.show()