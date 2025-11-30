# Colored prompt: username/dir:
PS1='\[\e[1;31m\]\u/\W: \[\e[0m\]'

# Function to check for command-not-found and suggest car
command_not_found_handle() {
    local cmd="$1"

    # Standard message fallback
    if [ -z "$cmd" ]; then
        return 127
    fi

    # Check .config/car/packagelist
    local list="$HOME/.config/car/packagelist"
    if [ -f "$list" ] && grep -qx "$cmd" "$list" 2>/dev/null; then
        echo "Command '$cmd' not found locally, but can be installed with:" >&2
        echo "    sudo car get $cmd" >&2
        echo "If you expected it to be installable, ensure car is initialized:" >&2
        echo "    car init" >&2
        echo "Then update lists regularly:" >&2
        echo "    car update" >&2
        echo "    car updatelist # if you do not want a full system update" >&2
        return 127
    fi

    echo "bash: $cmd: command not found" >&2
    return 127
}

# Source global definitions if present
[ -f /etc/bashrc ] && . /etc/bashrc
