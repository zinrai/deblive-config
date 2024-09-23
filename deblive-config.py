#!/usr/bin/env python3

import sys
import subprocess
import shlex
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="deblive-config",
        description="A wrapper for lb config to simplify Debian Live Build configuration"
    )
    parser.add_argument("--distribution", default="sid", help="Distribution (default: sid)")
    parser.add_argument("--architecture", default="amd64", help="Architecture (default: amd64)")
    parser.add_argument("--binary-images", default="iso-hybrid", help="Binary images (default: iso-hybrid)")
    parser.add_argument("--archive-areas", default="main", help="Archive areas (default: main)")
    parser.add_argument("--apt-indices", default="true", help="Apt indices (default: true)")
    parser.add_argument("--mirror-bootstrap", default="http://httpredir.debian.org/debian", help="Mirror bootstrap (default: http://httpredir.debian.org/debian)")
    parser.add_argument("--mirror-binary", default="http://httpredir.debian.org/debian", help="Mirror binary (default: http://httpredir.debian.org/debian)")
    parser.add_argument("--packages", help="Additional packages to include (comma-separated)")

    return parser.parse_known_args()

def print_command(cmd):
    print("Executing command:", file=sys.stderr)
    print(shlex.join(cmd), file=sys.stdout)

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: lb config command failed with return code {e.returncode}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: lb config command not found. Make sure live-build is installed.", file=sys.stderr)
        sys.exit(1)

def add_packages_to_list(packages):
    package_list_file = "config/package-lists/debliveconfig.list.chroot"
    os.makedirs(os.path.dirname(package_list_file), exist_ok=True)
    with open(package_list_file, "w") as f:
        f.write("\n".join(packages.split(",")))
    print(f"Created package list file: {package_list_file}", file=sys.stderr)
    print(f"Added the following packages:", file=sys.stderr)
    print(packages, file=sys.stderr)

def main():
    args, unknown = parse_arguments()

    # Create the base command with default options
    cmd = [
        "lb", "config",
        "--distribution", args.distribution,
        "--architecture", args.architecture,
        "--binary-images", args.binary_images,
        "--archive-areas", args.archive_areas,
        "--apt-indices", args.apt_indices,
        "--mirror-bootstrap", args.mirror_bootstrap,
        "--mirror-binary", args.mirror_binary
    ]

    # Add unknown arguments directly to the command
    if unknown:
        # Remove the leading '--' if present
        if unknown[0] == '--':
            unknown = unknown[1:]
        cmd.extend(unknown)

    print_command(cmd)

    # Run lb config and wait for it to complete
    run_command(cmd)

    # After lb config has completed, add packages to the list if specified
    if args.packages:
        add_packages_to_list(args.packages)

if __name__ == "__main__":
    main()
