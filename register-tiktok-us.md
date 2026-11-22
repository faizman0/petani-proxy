# Register TikTok US via Proxy (Manual, Lo Yang Klik)

## Proxy lo (dari PetaniProxy, 3 US)
| # | Proxy | IP | Kota |
|---|---|---|---|
| 1 | http://agaulicr:gkgjy6rwczp0@198.23.243.226:6361 | 198.23.243.226 | US Los Angeles |
| 2 | http://agaulicr:gkgjy6rwczp0@38.154.185.97:6370 | 38.154.185.97 | US Piscataway |
| 3 | http://agaulicr:gkgjy6rwczp0@191.96.254.138:6185 | 191.96.254.138 | US Los Angeles |

User:pass kedua (kalau agaulicr limit): `rppzxmnw:ux0v4zouts7g`

## Langkah 0 — Test proxy (liat sendiri)
```bash
cd /Users/faiz/Project/petani-proxy
for u in "agaulicr:gkgjy6rwczp0@198.23.243.226:6361" \
         "agaulicr:gkgjy6rwczp0@38.154.185.97:6370" \
         "agaulicr:gkgjy6rwczp0@191.96.254.138:6185"; do
  ip=$(echo "$u" | sed 's/.*@//;s/:[0-9]*$//')
  r=$(curl -s --max-time 20 -x "http://$u" https://ipify.org 2>/dev/null)
  if [ -n "$r" ] && [ "$r" != "Bandwidth limit reached. Please upgrade to continue using the proxy." ]; then
    geo=$(curl -s --max-time 5 "https://ipinfo.io/$r" | python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('country','?'),d.get('city','?'))" 2>/dev/null)
    echo "HIDUP: $ip -> keluar $r ($geo)"
  else
    echo "LIMIT: $ip -> kuota habis"
  fi
done
```
Pilih 1 yang HIDUP + negara US.

## Langkah 1 — Set proxy di browser (Chrome)
Opsi A (paling gampang): extension **SwitchyOmega**
```
1. Install SwitchyOmega (Chrome Web Store)
2. Profile baru: "US-1"
   - Type: Manual Proxy
   - HTTP: 198.23.243.226  Port: 6361
   - Proxy auth (kalau ditanya): user=agaulicr pass=gkgjy6rwczp0
3. Set US-1 as default, atau pake tombol SwitchyOmega per tab
```
Opsi B (tanpa extension): Chrome flag
```
chrome://flags → "Proxy server" → 198.23.243.226:6361
Restart Chrome
```

## Langkah 2 — Verifikasi proxy bener US
```
1. Buka https://ipify.org → harus keluar 198.23.243.226
2. Buka https://ipinfo.io → negara = US, kota = Los Angeles
3. Kalau keluar IP beda / negara Indo → proxy gak jalan, balik Langkah 0
```

## Langkah 3 — Register TikTok (1 account)
```
1. Browser (proxy US-1) → https://www.tiktok.com
2. Sign up → email + password lo (bukan burner)
3. Nama: [lo mau]  Username: [lo mau]
4. Region: United States  (jangan Indo)
5. Verifikasi email → login ulang, pastikan tetap via proxy US-1
6. Selesai. Account 1 = IP 198.23.243.226 (US LA) selamanya
```

## Langkah 4 — Register TikTok (account 2, 3)
```
- Account 2: proxy US-2 (38.154.185.97) → register via proxy US-2
- Account 3: proxy US-3 (191.96.254.138) → register via proxy US-3
- 1 account = 1 IP. Jangan campur.
- Browser: 1 profile per account (SwitchyOmega, atau 3 Chrome profile terpisah)
```

## Langkah 5 — Upload
Lo pilih 1:
- **Upload-Post $24**: register app.upload-post.com, connect TikTok lo, API key → AutoClip `.env` UPLOAD_POST_API_KEY.
- **Bypass (gue bikinin module)**: register TikTok for Developers app + OAuth, AutoClip upload langsung, gak pake Upload-Post.

## Note
- Proxy Webshare free = bandwidth limit. Kalau semua "LIMIT", lo pake user:pass kedua (rppzxmnw) atau register Webshare US sendiri ($2–3) buat kuota penuh.
- IP register (US) harus sama dengan IP upload (kalau via Upload-Post = DE, kalau via TikTok API dari mac = Indo). Lo putusin.
- Jangan upload dari IP Indo kalau lo mau TikTok anggap lo US.
