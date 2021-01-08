import sys

def main(file):
	print("==Community ID Scrubber==")
	with open(file, "rb+") as f:
		level_version = f.read(1)
		if not level_version >= bytes(0) and level_version <= bytes(29):
			print("[ERROR] File isn't a Principia level or has an unsupported level version.")
		level_type = f.read(1)
		level_community_id = f.read(4)
		print("Level version: 0x%s" % level_version.hex())
		print("Community ID: 0x%s" % level_community_id.hex())
		print("Changing community ID to 0x00000000")
		f.seek(2)
		f.write(b"\00\00\00\00")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python scrubber.py [filename]")
	else:
		main(sys.argv[1])
