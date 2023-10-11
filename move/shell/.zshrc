# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Lines configured by zsh-newuser-install
HISTFILE=~/.config/zsh/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v

# Specify default editor. Possible values: vim, nano, ed etc.
export EDITOR=nvim

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/spidy/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Plugins
# powerlevel10k
source $HOME/.config/zsh/plugins/powerlevel10k/powerlevel10k.zsh-theme
# autosuggestions
source $HOME/.config/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
# syntax-highligting
source $HOME/.config/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


# Aliases
alias "py_env"="python -m venv"

alias "cc"="clear"

alias "."="cd .."
alias ".."="cd ../.."
alias "..."="cd ../../.."
alias "ll"="exa -la"
