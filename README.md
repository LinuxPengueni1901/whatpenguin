# WhatPenguin

WhatPenguin, Linux masaüstü ortamları (GNOME, vb.) için tasarlanmış, GTK4 ve WebKit teknolojilerini kullanan modern bir WhatsApp Web istemcisidir.

## Özellikler

- **Modern Arayüz**: Libadwaita kullanarak GNOME masaüstü ile uyumlu şık görünüm.
- **Yerel Entegrasyon**: Masaüstü menüsünde yer alır.
- **Hafif**: WebKit motorunu kullanarak hızlı ve hafif bir deneyim sunar.
- **Gizlilik**: Standart WhatsApp Web trafiği dışında veri toplamaz.

## Gereksinimler

- Python 3
- GTK 4
- Libadwaita
- WebKitGTK 6.0
- PyGObject

## Kurulum ve Çalıştırma

1. Bağımlılıkları yükleyin (Ubuntu/Debian örneği):
   ```bash
   sudo apt install python3-gi python3-adwaita gir1.2-webkit-6.0
   ```

2. Depoyu klonlayın veya indirin.

3. Uygulamayı çalıştırın:
   ```bash
   python3 main.py
   ```

## Masaüstü Kısayolu

`whatpenguin.desktop` dosyasını `~/.local/share/applications/` dizinine kopyalayarak uygulama menüsüne ekleyebilirsiniz:

```bash
cp whatpenguin.desktop ~/.local/share/applications/
```

**Not:** Masaüstündeki kısayol ikonuna sağ tıklayıp "Allow Launching" seçeneğini seçmeniz gerekebilir.

## Flatpak (Geliştirici)

Proje Flatpak paketlemesi için `com.taha.whatpenguin.yml` manifest dosyasını içerir. `flatpak-builder` ile yerel testler yapılabilir.

## Lisans

Bu proje açık kaynaklıdır ve eğitim amaçlı geliştirilmiştir. WhatsApp, Meta Platforms, Inc.'in tescilli markasıdır.
