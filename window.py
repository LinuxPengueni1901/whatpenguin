import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('WebKit', '6.0')

import os
from gi.repository import Gtk, Adw, WebKit, Gdk

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title("WhatPenguin")
        self.set_default_size(1000, 700)
        
        # İkonu ayarla
        try:
            display = Gdk.Display.get_default()
            icon_theme = Gtk.IconTheme.get_for_display(display)
            # Hem sistem ikonlarını hem de bulunduğumuz dizini ara
            current_dir = os.path.dirname(os.path.abspath(__file__))
            icon_theme.add_search_path(current_dir)
            
            # Sistem dizinine yüklenmemişse bile buradan bulabilir
            if os.path.exists(os.path.join(current_dir, "whatpenguin.png")):
                 icon_theme.add_resource_path(current_dir)

            self.set_icon_name("whatpenguin")
        except Exception as e:
            print(f"Ikon yuklenirken hata: {e}")
            # Fallback
            self.set_icon_name("whatpenguin")

        # Ana içerik kutusu
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(box)

        # Header Bar
        header = Adw.HeaderBar()
        box.append(header)

        # Yenileme Butonu
        reload_button = Gtk.Button(icon_name="view-refresh-symbolic")
        reload_button.set_tooltip_text("Yenile")
        reload_button.connect("clicked", self.on_reload_clicked)
        header.pack_end(reload_button)

        # WebView
        self.webview = WebKit.WebView()
        
        # navigator.platform değerini Win32 olarak değiştir (Mac algılanmasını önlemek için)
        content_manager = self.webview.get_user_content_manager()
        script = WebKit.UserScript(
            source="Object.defineProperty(navigator, 'platform', {get: function(){return 'Win32';}});",
            injected_frames=WebKit.UserContentInjectedFrames.TOP_FRAME,
            injection_time=WebKit.UserScriptInjectionTime.START,
            allow_list=[],
            block_list=[]
        )
        content_manager.add_script(script)
        
        # WhatsApp Web için gerekli ayarlar
        settings = self.webview.get_settings()
        settings.set_enable_javascript(True)
        settings.set_enable_developer_extras(True) # Geliştirici araçları (incele vs)

        # User-Agent'ı Windows/Chrome gibi göster
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        settings.set_user_agent(user_agent)

        # Genişlet ve doldur
        self.webview.set_vexpand(True)
        self.webview.set_hexpand(True)
        
        box.append(self.webview)

        # URL'yi yükle
        self.webview.load_uri("https://web.whatsapp.com")
        
        # İzin isteklerini yönet (Bildirim, Mikrofon vb.)
        self.webview.connect("permission-request", self.on_permission_request)

    def on_permission_request(self, webview, request):
        # Şimdilik tüm izinleri kabul et (Bildirimler vb. için)
        # Daha sonra kullanıcıya sormak için dialog eklenebilir.
        request.allow()
        return True

    def on_reload_clicked(self, button):
        self.webview.reload()
