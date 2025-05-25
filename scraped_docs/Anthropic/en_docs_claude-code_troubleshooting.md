---
url: https://docs.anthropic.com/en/docs/claude-code/troubleshooting
scraped_at: 2025-05-24T19:39:03.245889
title: Troubleshooting - Anthropic
---

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
⌘K
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Go to claude.ai](https://claude.ai/)
  * [Go to claude.ai](https://claude.ai/)


Search...
Navigation
Claude Code
Troubleshooting
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### Claude Code
  * [Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
  * [Getting started](https://docs.anthropic.com/en/docs/claude-code/getting-started)
  * [Common tasks](https://docs.anthropic.com/en/docs/claude-code/common-tasks)
  * [CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
  * [IDE integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
  * [Memory management](https://docs.anthropic.com/en/docs/claude-code/memory)
  * [Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
  * [Security](https://docs.anthropic.com/en/docs/claude-code/security)
  * [Team setup](https://docs.anthropic.com/en/docs/claude-code/team)
  * [Monitoring usage](https://docs.anthropic.com/en/docs/claude-code/monitoring-usage)
  * [Costs](https://docs.anthropic.com/en/docs/claude-code/costs)
  * [Bedrock, Vertex, and proxies](https://docs.anthropic.com/en/docs/claude-code/bedrock-vertex-proxies)
  * [GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)
  * [SDK](https://docs.anthropic.com/en/docs/claude-code/sdk)
  * [Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)
  * [Troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)


Claude Code
# Troubleshooting
Solutions for common issues with Claude Code installation and usage.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#common-installation-issues)
Common installation issues
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-permission-issues)
Linux permission issues
When installing Claude Code with npm, you may encounter permission errors if your npm global prefix is not user writable (eg. `/usr`, or `/use/local`).
#### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution%3A-create-a-user-writable-npm-prefix)
Recommended solution: Create a user-writable npm prefix
The safest approach is to configure npm to use a directory within your home folder:
Copy
```
# First, save a list of your existing global packages for later migration
npm list -g --depth=0 > ~/npm-global-packages.txt
# Create a directory for your global packages
mkdir -p ~/.npm-global
# Configure npm to use the new directory path
npm config set prefix ~/.npm-global
# Note: Replace ~/.bashrc with ~/.zshrc, ~/.profile, or other appropriate file for your shell
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
# Apply the new PATH setting
source ~/.bashrc
# Now reinstall Claude Code in the new location
npm install -g @anthropic-ai/claude-code
# Optional: Reinstall your previous global packages in the new location
# Look at ~/npm-global-packages.txt and install packages you want to keep

```

This solution is recommended because it:
  * Avoids modifying system directory permissions
  * Creates a clean, dedicated location for your global npm packages
  * Follows security best practices


#### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#system-recovery%3A-if-you-have-run-commands-that-change-ownership-and-permissions-of-system-files-or-similar)
System Recovery: If you have run commands that change ownership and permissions of system files or similar
If you’ve already run a command that changed system directory permissions (such as `sudo chown -R $USER:$(id -gn) /usr && sudo chmod -R u+w /usr`) and your system is now broken (for example, if you see `sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set`), you’ll need to perform recovery steps.
##### Ubuntu/Debian Recovery Method:
  1. While rebooting, hold **SHIFT** to access the GRUB menu
  2. Select “Advanced options for Ubuntu/Debian”
  3. Choose the recovery mode option
  4. Select “Drop to root shell prompt”
  5. Remount the filesystem as writable:
Copy
```
mount -o remount,rw /

```

  6. Fix permissions:
Copy
```
# Restore root ownership
chown -R root:root /usr
chmod -R 755 /usr
# Ensure /usr/local is owned by your user for npm packages
chown -R YOUR_USERNAME:YOUR_USERNAME /usr/local
# Set setuid bit for critical binaries
chmod u+s /usr/bin/sudo
chmod 4755 /usr/bin/sudo
chmod u+s /usr/bin/su
chmod u+s /usr/bin/passwd
chmod u+s /usr/bin/newgrp
chmod u+s /usr/bin/gpasswd
chmod u+s /usr/bin/chsh
chmod u+s /usr/bin/chfn
# Fix sudo configuration
chown root:root /usr/libexec/sudo/sudoers.so
chmod 4755 /usr/libexec/sudo/sudoers.so
chown root:root /etc/sudo.conf
chmod 644 /etc/sudo.conf

```

  7. Reinstall affected packages (optional but recommended):
Copy
```
# Save list of installed packages
dpkg --get-selections > /tmp/installed_packages.txt
# Reinstall them
awk '{print $1}' /tmp/installed_packages.txt | xargs -r apt-get install --reinstall -y

```

  8. Reboot:
Copy
```
reboot

```



##### Alternative Live USB Recovery Method:
If the recovery mode doesn’t work, you can use a live USB:
  1. Boot from a live USB (Ubuntu, Debian, or any Linux distribution)
  2. Find your system partition:
Copy
```
lsblk

```

  3. Mount your system partition:
Copy
```
sudo mount /dev/sdXY /mnt # replace sdXY with your actual system partition

```

  4. If you have a separate boot partition, mount it too:
Copy
```
sudo mount /dev/sdXZ /mnt/boot # if needed

```

  5. Chroot into your system:
Copy
```
# For Ubuntu/Debian:
sudo chroot /mnt
# For Arch-based systems:
sudo arch-chroot /mnt

```

  6. Follow steps 6-8 from the Ubuntu/Debian recovery method above


After restoring your system, follow the recommended solution above to set up a user-writable npm prefix.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#auto-updater-issues)
Auto-updater issues
If Claude Code can’t update automatically, it may be due to permission issues with your npm global prefix directory. Follow the [recommended solution](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution-create-a-user-writable-npm-prefix) above to fix this.
If you prefer to disable the auto-updater instead, you can use:
Copy
```
claude config set -g autoUpdaterStatus disabled

```

## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#permissions-and-authentication)
Permissions and authentication
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#repeated-permission-prompts)
Repeated permission prompts
If you find yourself repeatedly approving the same commands, you can allow specific tools to run without approval:
Copy
```
# Let npm test run without approval
claude config add allowedTools "Bash(npm test)"
# Let npm test and any of its sub-commands run without approval
claude config add allowedTools "Bash(npm test:*)"

```

### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#authentication-issues)
Authentication issues
If you’re experiencing authentication problems:
  1. Run `/logout` to sign out completely
  2. Close Claude Code
  3. Restart with `claude` and complete the authentication process again


If problems persist, try:
Copy
```
rm -rf ~/.config/claude-code/auth.json
claude

```

This removes your stored authentication information and forces a clean login.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#performance-and-stability)
Performance and stability
### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#high-cpu-or-memory-usage)
High CPU or memory usage
Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues:
  1. Use `/compact` regularly to reduce context size
  2. Close and restart Claude Code between major tasks
  3. Consider adding large build directories to your `.gitignore` file


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#command-hangs-or-freezes)
Command hangs or freezes
If Claude Code seems unresponsive:
  1. Press Ctrl+C to attempt to cancel the current operation
  2. If unresponsive, you may need to close the terminal and restart


### 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#esc-key-not-working-in-jetbrains-intellij%2C-pycharm%2C-etc-terminals)
ESC key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals
If you’re using Claude Code in JetBrains terminals and the ESC key doesn’t interrupt the agent as expected, this is likely due to a keybinding clash with JetBrains’ default shortcuts.
To fix this issue:
  1. Go to Settings → Tools → Terminal
  2. Click the “Configure terminal keybindings” hyperlink next to “Override IDE Shortcuts”
  3. Within the terminal keybindings, scroll down to “Switch focus to Editor” and delete that shortcut


This will allow the ESC key to properly function for canceling Claude Code operations instead of being captured by PyCharm’s “Switch focus to Editor” action.
## 
[​](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#getting-more-help)
Getting more help
If you’re experiencing issues not covered here:
  1. Use the `/bug` command within Claude Code to report problems directly to Anthropic
  2. Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
  3. Run `/doctor` to check the health of your Claude Code installation


Was this page helpful?
YesNo
[Tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Common installation issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#common-installation-issues)
  * [Linux permission issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#linux-permission-issues)
  * [Recommended solution: Create a user-writable npm prefix](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#recommended-solution%3A-create-a-user-writable-npm-prefix)
  * [System Recovery: If you have run commands that change ownership and permissions of system files or similar](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#system-recovery%3A-if-you-have-run-commands-that-change-ownership-and-permissions-of-system-files-or-similar)
  * [Auto-updater issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#auto-updater-issues)
  * [Permissions and authentication](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#permissions-and-authentication)
  * [Repeated permission prompts](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#repeated-permission-prompts)
  * [Authentication issues](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#authentication-issues)
  * [Performance and stability](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#performance-and-stability)
  * [High CPU or memory usage](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#high-cpu-or-memory-usage)
  * [Command hangs or freezes](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#command-hangs-or-freezes)
  * [ESC key not working in JetBrains (IntelliJ, PyCharm, etc.) terminals](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#esc-key-not-working-in-jetbrains-intellij%2C-pycharm%2C-etc-terminals)
  * [Getting more help](https://docs.anthropic.com/en/docs/claude-code/troubleshooting#getting-more-help)



