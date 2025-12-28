#!/bin/bash
# install.sh
mkdir -p /app/bin
mkdir -p /app/share/whatpenguin
mkdir -p /app/share/applications
mkdir -p /app/share/icons/hicolor/128x128/apps

mkdir -p /app/share/metainfo

install -m 755 main.py /app/share/whatpenguin/
install -m 644 window.py /app/share/whatpenguin/
install -m 644 whatpenguin.png /app/share/whatpenguin/
# İkonu AppID ismiyle kopyala (Flathub gereksinimi)
install -m 644 whatpenguin.png /app/share/icons/hicolor/128x128/apps/io.github.linuxpengueni1901.whatpenguin.png

# Desktop file
install -m 644 io.github.linuxpengueni1901.whatpenguin.desktop /app/share/applications/

# Metainfo
install -m 644 io.github.linuxpengueni1901.whatpenguin.metainfo.xml /app/share/metainfo/

# Wrapper script
echo "#!/bin/bash" > /app/bin/whatpenguin
echo "exec python3 /app/share/whatpenguin/main.py \"\$@\"" >> /app/bin/whatpenguin
chmod +x /app/bin/whatpenguin
