"""
mnist database using my own method
"""
import urllib.request
import os.path
import mnist
import gzip
datasets_url = mnist.datasets_url

print(datasets_url)

def download(name):
  """
  also unzips
  """
  temp = os.path.join('/tmp/mnist', name)
  if os.path.isfile(temp):
    print('using cached file')
    return temp

  url = os.path.join(datasets_url , name)
  print(url)
  res = urllib.request.urlopen(url)
  data = res.read()

  os.makedirs('/tmp/mnist', exist_ok=True)
  with open(temp, 'wb') as file:
    file.write(data)
  return temp

def parse_3_dimensions(file):
    images = int.from_bytes(file.read(4),'big')
    rows = int.from_bytes(file.read(4),'big')
    columns = int.from_bytes(file.read(4),'big')
    res = [[[None for i in range(columns)] for j in range(rows)] for k in range(images)]
    for image in range( images ):
      for row in range( rows ):
        for col in range( columns ):
          res[image][row][col] = int.from_bytes(file.read(1),'big')
    return res

def parse_1_dimension(file):
    images = int.from_bytes(file.read(4),'big')
    res = [None for k in range(images)]
    for image in range( images ):
        res[image] = int.from_bytes(file.read(1),'big')
    return res
def parse(filename):
  with gzip.open(filename, 'rb') as file:
    assert file.read(3) == b'\x00\x00\x08' # 8 -> unsigned int; 0x03 -> 3 dimensions
    dimensions = int.from_bytes(file.read(1),'big')
    return {3: parse_3_dimensions, 1: parse_1_dimension}[dimensions](file)

def test_images():
  test_images_file = download('t10k-images-idx3-ubyte.gz')
  test_images = parse(test_images_file)
  assert len(test_images)== 10000
  assert len(test_images[0])== 28
  assert len(test_images[0][0])== 28
  assert isinstance(test_images[0][0][0], int)

def test_labels():
  test_labels_file = download('t10k-labels-idx1-ubyte.gz')
  test_labels = parse(test_labels_file)
  assert len(test_labels)== 10000
  assert isinstance(test_labels[0], int)


def test_train_images():
  test_images_file = download('train-images-idx3-ubyte.gz')
  test_images = parse(test_images_file)
  assert len(test_images)== 60000
  assert len(test_images[0])== 28
  assert len(test_images[0][0])== 28
  assert isinstance(test_images[0][0][0], int)

def test_train_labels():
  test_labels_file = download('train-labels-idx1-ubyte.gz')
  test_labels = parse(test_labels_file)
  assert len(test_labels)== 60000
  assert isinstance(test_labels[0], int)
