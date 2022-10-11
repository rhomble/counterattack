import argparse
from counterattack.obj.club import Club


def main():
    if FLAGS.export_squad_size == 'full':
        size = 00
    else:
        size = int(FLAGS.export_squad_size)
    Club(url=FLAGS.url, export_dir=FLAGS.export_dir, export_squad_size=size)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        type=str,
        default=None,
        help="name of magic expansion corresponding to data files"
    )
    parser.add_argument(
        "--export_dir",
        type=str,
        default=None,
        help="path to directory where file will be saved"
    )
    parser.add_argument(
        "--export_squad_size",
        type=str,
        default='25',
        help="either a number (meaning the top specified number of players) OR 'full' meaning the full squad."
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()