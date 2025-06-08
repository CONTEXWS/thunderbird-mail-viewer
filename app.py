import streamlit as st
import mailbox

# Thunderbird'in INBOX mbox dosyasının yolu - SENİN BİLGİSAYARINDA DEĞİŞTİR
MAILBOX_PATH = "C:\Users\Hp\AppData\Roaming\thunderbird\Profiles\ekn38stx.default-release\ImapMail\ukpro3.fcomet.com"

st.set_page_config(page_title="📧 Thunderbird Mail Viewer", layout="centered")

st.title("📧 Müşteri E-Posta Özeti")
st.markdown("Thunderbird'de yerel olarak saklanan e-postaların konularını görüntüler.")

try:
    mbox = mailbox.mbox(MAILBOX_PATH)

    if len(mbox) == 0:
        st.warning("Hiç e-posta bulunamadı.")
    else:
        st.write(f"Toplam {len(mbox)} e-posta bulundu:")
        for i, message in enumerate(mbox):
            sender = message['from'] or "Bilinmiyor"
            subject = message['subject'] or "(Konu Yok)"
            body_snippet = message.get_payload(decode=True).decode('utf-8', errors='ignore')[:200]

            with st.expander(f"{i+1}. {sender} – {subject}"):
                st.markdown("**İlk içerik:**")
                st.text(body_snippet)

except Exception as e:
    st.error(f"E-posta okuma hatası: {str(e)}")
    st.info("Lütfen MAILBOX_PATH doğru yol gösteriyor mu diye kontrol edin.")
