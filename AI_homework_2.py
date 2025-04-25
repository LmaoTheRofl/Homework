import numpy as np

def add_padding(image, padding_size):

    batch_size, channels, height, size = image.shape
    padded_height = height + 2 * padding_size
    padded_size = size + 2 * padding_size

    padded_batch = np.zeros((batch_size, channels, padded_height, padded_size))
    
    padded_batch[:, :, padding_size:padding_size+height, padding_size:padding_size+size] = image
    
    return padded_batch




def convolve(image, kernel):

    kernel_height, kernel_size = kernel.shape
    image_height, image_size = image.shape

    output_height = image_height - kernel_height + 1
    output_size = image_size - kernel_size + 1
    
    output = np.zeros((output_height, output_size))
    
    for i in range(output_height):
        for j in range(output_size):
            output[i, j] = np.sum(image[i:i + kernel_height, j:j + kernel_size] * kernel)
    
    return output




def pooling(image, pool_size):
    pool_height, pool_size = pool_size
    image_height, image_size = image.shape
    
    
    output_height = image_height // pool_height
    output_size = image_size // pool_size
    
    
    output = np.zeros((output_height, output_size))
    
    
    for i in range(output_height):
        for j in range(output_size):
            output[i, j] = np.max(image[i * pool_height:(i + 1) * pool_height,
                                        j * pool_size:(j + 1) * pool_size])
    
    return output


