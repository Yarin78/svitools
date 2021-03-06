import sys
import os
import os.path
import logging

from disk import Disk
import basic_tokenizer

def extract(disk_image, output_path):
    disk = Disk(disk_image)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not disk.has_fat():
        logging.info("Skipping %s, has no FAT" % os.path.basename(disk_image))
        return
    logging.info('Extracting %s' % os.path.basename(disk_image))
    for f in disk.get_files():
        if f.is_basic_file():
            data = disk.read_file(f)
            logging.info("Detokenizing %s" % f.filename)
            lines = basic_tokenizer.detokenize(data)
            with open(os.path.join(output_path, f.filename), "wt") as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')


def main():
    #extract('/Users/yarin/Dropbox/SVI/Disk/tokentest.dsk', '/Users/yarin/src/svitools/tokentest')
    #extract('/Users/yarin/Dropbox/SVI/Disk/ripped/80-disk3.dsk', '/Users/yarin/src/svitools/80-disk3')
    #extract('/Users/yarin/Dropbox/SVI/Disk/ripped/musik.dsk', '/Users/yarin/src/svitools/musik')
    #extract('/Users/yarin/Dropbox/SVI/Disk/ripped/disk1.dsk', '/Users/yarin/src/svitools/disk1')
    inpath = '/Users/yarin/Dropbox/SVI/Disk/ripped/'
    outpathroot = '/Users/yarin/src/svitools/out/'
    for f in os.listdir(inpath):
        (root, ext) = os.path.splitext(f)
        if ext == '.dsk':
            infile = os.path.join(inpath, f)
            outpath = os.path.join(outpathroot, root)
            #print infile, outpath
            extract(infile, outpath)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
