#!/bin/bash

function find_root_dir_with_readme {
    # Set the starting directory to the current directory
    dir=$(pwd)
    # Loop until we reach the root directory
    while [[ "$dir" != "/" ]]; do
        # Check if the current directory contains a file named README.md
        if [[ -f "$dir/README.md" ]]; then
            # Return the path to the root directory containing README.md
            echo "$dir"
            return 0
        fi
        # Move up one directory
        dir=$(dirname "$dir")
    done
    return 1
}

# This function searches for proto files in a directory and builds python grpc compaitable with the same
function build_proto_files {
    proto_dirs=$(find proto -type f -name '*.proto' -exec dirname {} \; | sort -u)
    for dir in $proto_dirs; do
        python3 \
            -m grpc_tools.protoc \
            -I proto \
            -I $dir \
            --python_betterproto_out=$root_dir/comdexpy/proto  \
            $(find "${dir}" -maxdepth 1 -name '*.proto')   
    done
}


# Call the function and store the result in a variable
root_dir=$(find_root_dir_with_readme)

# Check if the function succeeded
if [[ $? -eq 1 ]]; then
    echo "Error: could not find root directory with README.md" >&2
    exit
fi

build_proto_files $root_dir/proto