from pathlib import Path
import os
import sys
import datetime
import tinify  # type: ignore


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"Time taken: {end - start} seconds")

    return wrapper


def main():
    # Clears the terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Quick script for using Tinify API to compress mass amounts of images
    if not Path(sys.argv[1]).is_dir():
        print("It seems like that directory doesn't exist. Please try again.")
        sys.exit(print(f"{sys.argv[1]} ||| Now exiting..."))

    print(f"{sys.argv[1]} is a valid directory!")

    try:
        tinify.key = sys.argv[2]
        tinify.validate()
    except tinify.AccountError:
        print("API key incorrect. Please try again.")
        sys.exit()

    print(f"{sys.argv[2]} is a valid API Key! Now to begin compressing...")
    compression(sys.argv[1], sys.argv[2])


@timer
def compression(directory: str, api_key: str) -> None:
    """Function used to compress images in the given directory.

    Args:
        directory (str): Directory that contains the images that need to be compressed.
        api_key (str): API Key that is provided by Tinify.
    """
    tinify.key = api_key

    print("\n")
    for filename in Path.iterdir(Path(directory)):
        if filename.glob("*.[jp][pn][ge][g]"):
            source = tinify.from_file(Path(filename))
            source.to_file(Path(filename))
            print(f"Compressing {filename}...")

        else:
            print(f"Skipping {filename}...")

    print(f"Done! All images in {directory} have been compressed.")
    print("\n")


if __name__ == "__main__":
    main()
