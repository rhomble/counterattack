import argparse
from counterattack.obj.player import Player


def main():
    Player(url=FLAGS.url, export_dir=FLAGS.export_dir)

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
    FLAGS, unparsed = parser.parse_known_args()
    main()