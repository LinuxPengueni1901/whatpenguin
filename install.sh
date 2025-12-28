#!/bin/bash
# install.sh
mkdir -p /app/bin
mkdir -p /app/share/whatpenguin
mkdir -p /app/share/applications
mkdir -p /app/share/icons/hicolor/128x128/apps

install -m 755 main.py /app/share/whatpenguin/
install -m 644 window.py /app/share/whatpenguin/
install -m 644 whatpenguin.png /app/share/whatpenguin/
install -m 644 whatpenguin.png /app/share/icons/hicolor/128x128/apps/whatpenguin.png

# Desktop file
install -m 644 whatpenguin.desktop /app/share/applications/

# Wrapper script
echo "#!/bin/bash" > /app/bin/whatpenguin
echo "exec python3 /app/share/whatpenguin/main.py \"\$@\"" >> /app/bin/whatpenguin
chmod +x /app/bin/whatpenguin
