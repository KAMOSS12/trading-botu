# Claude Code Komut Referansı

## Input Prefix'leri

| Prefix | Açıklama |
|--------|----------|
| `/` | Slash komutlarına, skill'lere ve MCP prompt'larına erişim |
| `!` | Bash modu — komutu doğrudan terminalde çalıştırır, çıktıyı konuşmaya ekler |
| `@` | Dosya yolu mention — dosya/dizin adı otomatik tamamlama tetikler |

---

## Slash Komutları

### Oturum & Navigasyon

| Komut | Açıklama |
|-------|----------|
| `/help` | Yardım ve mevcut komutları göster |
| `/clear` | Konuşma geçmişini temizle ve context'i serbest bırak |
| `/exit` | CLI'dan çık (alias: `/quit`) |
| `/resume [session]` | Oturumu ID veya isimle devam ettir |
| `/rename [isim]` | Mevcut oturumu yeniden adlandır |
| `/fork [isim]` | Bu noktada konuşmanın bir fork'unu oluştur |
| `/rewind` | Konuşmayı ve/veya kodu önceki bir noktaya geri al (alias: `/checkpoint`) |

### Kod & Dosya Yönetimi

| Komut | Açıklama |
|-------|----------|
| `/diff` | Kaydedilmemiş değişiklikleri interaktif diff görüntüleyicide aç |
| `/export [dosyaadı]` | Konuşmayı düz metin olarak dışa aktar |
| `/copy` | Son asistan yanıtını panoya kopyala |

### Yapılandırma & Ayarlar

| Komut | Açıklama |
|-------|----------|
| `/config` | Ayarlar arayüzünü aç (alias: `/settings`) |
| `/model [model]` | AI modelini seç veya değiştir |
| `/theme` | Renk temasını değiştir |
| `/keybindings` | Klavye kısayolları yapılandırma dosyasını aç/oluştur |
| `/statusline` | Status line'ı yapılandır |
| `/permissions` | İzinleri görüntüle veya güncelle (alias: `/allowed-tools`) |
| `/sandbox` | Sandbox modunu aç/kapat |

### Context & Performans

| Komut | Açıklama |
|-------|----------|
| `/context` | Mevcut context kullanımını görselleştir |
| `/cost` | Token kullanım istatistiklerini göster |
| `/compact [talimatlar]` | Konuşmayı isteğe bağlı odak talimatlarıyla sıkıştır |

### Modlar & Özellikler

| Komut | Açıklama |
|-------|----------|
| `/plan` | Plan modunu etkinleştir |
| `/fast [on\|off]` | Hızlı modu aç/kapat |
| `/vim` | Vim ve Normal düzenleme modları arasında geçiş yap |

### Proje & Başlatma

| Komut | Açıklama |
|-------|----------|
| `/init` | `CLAUDE.md` ile projeyi başlat |
| `/add-dir <yol>` | Mevcut oturuma yeni bir çalışma dizini ekle |
| `/agents` | Agent/subagent yapılandırmalarını yönet |
| `/skills` | Mevcut skill'leri listele |
| `/hooks` | Hook yapılandırmalarını yönet |
| `/mcp` | MCP sunucu bağlantılarını yönet |
| `/memory` | `CLAUDE.md` bellek dosyalarını düzenle |

### Kod İnceleme & Otomasyon

| Komut | Açıklama |
|-------|----------|
| `/pr-comments [PR]` | GitHub pull request yorumlarını getir |
| `/security-review` | Bekleyen değişiklikleri güvenlik açıkları için analiz et |
| `/review` | Pull request incele |

### Entegrasyon & Araçlar

| Komut | Açıklama |
|-------|----------|
| `/ide` | IDE entegrasyonlarını yönet |
| `/install-github-app` | Claude GitHub Actions uygulamasını kur |
| `/desktop` | Oturumu Claude Code Desktop uygulamasında devam ettir (alias: `/app`) |
| `/remote-control` | Bu oturumu claude.ai'dan uzak kontrole aç (alias: `/rc`) |

### Kimlik Doğrulama & Hesap

| Komut | Açıklama |
|-------|----------|
| `/login` | Anthropic hesabına giriş yap |
| `/logout` | Anthropic hesabından çıkış yap |
| `/usage` | Plan kullanım limitlerini göster |
| `/upgrade` | Üst plan katmanına yükselt |

### Sistem & Tanılama

| Komut | Açıklama |
|-------|----------|
| `/doctor` | Claude Code kurulumunu ve ayarlarını teşhis et |
| `/status` | Sürüm, model, hesap ve bağlantı durumunu göster |
| `/stats` | Günlük kullanım ve oturum geçmişini görselleştir |
| `/insights` | Claude Code oturumlarını analiz eden rapor oluştur |
| `/release-notes` | Tam changelog'u görüntüle |
| `/feedback` | Claude Code hakkında geri bildirim gönder (alias: `/bug`) |
| `/btw <soru>` | Konuşmaya eklemeden hızlı yan soru sor |

---

## Klavye Kısayolları

### Genel Kontroller

| Kısayol | Açıklama |
|---------|----------|
| `Ctrl+C` | Mevcut girişi veya oluşturmayı iptal et |
| `Ctrl+D` | Claude Code oturumundan çık |
| `Ctrl+L` | Terminal ekranını temizle (konuşma geçmişi korunur) |
| `Ctrl+O` | Ayrıntılı araç kullanımını göster/gizle |
| `Ctrl+R` | Komut geçmişinde ters arama |
| `Ctrl+B` | Çalışan görevleri arka plana al |
| `Ctrl+T` | Görev listesini aç/kapat |
| `Ctrl+G` | Varsayılan metin düzenleyicide aç |
| `Ctrl+F` | Tüm arka plan agent'larını durdur (3 saniye içinde iki kez) |
| `Shift+Tab` / `Alt+M` | İzin modları arasında geçiş yap (Auto-Accept / Plan / Normal) |
| `Alt+P` | Model değiştir (prompt'u temizlemeden) |
| `Alt+T` | Genişletilmiş düşünme modunu aç/kapat |
| `Esc Esc` | Geri al veya özetle |

### Metin Düzenleme

| Kısayol | Açıklama |
|---------|----------|
| `Ctrl+K` | İmlecten satır sonuna kadar sil |
| `Ctrl+U` | Tüm satırı sil |
| `Ctrl+Y` | Silinen metni yapıştır |
| `Alt+B` | Bir kelime geri git |
| `Alt+F` | Bir kelime ileri git |

### Çok Satırlı Giriş

| Yöntem | Kısayol |
|--------|---------|
| Evrensel | `\` + `Enter` |
| macOS | `Option+Enter` |
| Terminale göre | `Shift+Enter` (iTerm2, WezTerm, Ghostty, Kitty) |
| Kontrol | `Ctrl+J` |

---

## Vim Modu Komutları (`/vim` ile etkinleştir)

### Mod Geçişleri

| Komut | Eylem |
|-------|-------|
| `Esc` | NORMAL moda geç |
| `i` | İmlecin önüne ekle |
| `I` | Satırın başına ekle |
| `a` | İmlecin arkasına ekle |
| `A` | Satırın sonuna ekle |
| `o` | Alt satıra aç |
| `O` | Üst satıra aç |

### Navigasyon (NORMAL mod)

| Komut | Eylem |
|-------|-------|
| `h/j/k/l` | Sol/aşağı/yukarı/sağ |
| `w/e/b` | Sonraki kelime / kelime sonu / önceki kelime |
| `0` / `$` | Satır başı / satır sonu |
| `gg` / `G` | Giriş başı / giriş sonu |
| `f{harf}` | Sonraki karaktere atla |

### Düzenleme (NORMAL mod)

| Komut | Eylem |
|-------|-------|
| `x` | Karakter sil |
| `dd` | Satır sil |
| `cc` | Satırı değiştir |
| `yy` | Satırı kopyala |
| `p` / `P` | İmlecin arkasına/önüne yapıştır |
| `.` | Son değişikliği tekrarla |
| `>>` / `<<` | Girintile / girintiyi geri al |
