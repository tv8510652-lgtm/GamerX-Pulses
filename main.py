import sys
import psutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

# محاكاة بسيطة للـ Unity Ads SDK على الأندرويد
class UnityAdsManager:
    def __init__(self):
        self.game_id = "800077499"
        self.banner_id = "Banner_Android"
        self.rewarded_id = "Rewarded_Android"
        self.initialized = False

    def initialize_ads(self):
        print(f"Initializing Unity Ads with Game ID: {self.game_id}")
        self.initialized = True
        self.show_banner()

    def show_banner(self):
        if self.initialized:
            print(f"Showing Banner Ad: {self.banner_id} at the bottom.")

    def show_rewarded(self, on_complete):
        if self.initialized:
            print(f"Triggering Rewarded Video Ad: {self.rewarded_id}")
            # عند انتهاء الإعلان بنجاح نقوم بتشغيل الدالة لإظهار البيانات المقفلة
            on_complete()

class GamerXPulseApp(App):
    def build(self):
        self.title = "GamerX Pulse"
        self.ads = UnityAdsManager()
        self.ads.initialize_ads()
        
        # الواجهة الرئيسية (ثيم جيمرز مظلم)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # تغيير خلفية الشاشة برمجياً إلى الأسود
        from kivy.core.window import Window
        Window.clearcolor = get_color_from_hex('#0A0A0A')

        # العنوان الرئيسي
        title_label = Label(
            text="GAMERX PULSE", 
            font_size='28sp', 
            bold=True, 
            color=get_color_from_hex('#00FF66') # أخضر نيوني
        )
        layout.add_widget(title_label)

        # عداد الفريمات (FPS Counter)
        self.fps_label = Label(text="Live FPS: Calculating...", font_size='20sp', color=get_color_from_hex('#00E5FF'))
        layout.add_widget(self.fps_label)
        Clock.schedule_interval(self.update_fps, 1.0 / 60.0) # تحديث مستمر

        # معلومات النظام (RAM)
        ram = psutil.virtual_memory()
        total_ram_gb = round(ram.total / (1024 ** 3), 1)
        self.ram_label = Label(
            text=f"Total RAM: {total_ram_gb} GB | Available RAM: Calculating...", 
            font_size='14sp'
        )
        layout.add_widget(self.ram_label)
        Clock.schedule_interval(self.update_ram, 2.0)

        # قسم توقع أداء الألعاب
        game_title = Label(text="--- Game Performance Predictor ---", font_size='16sp', color=get_color_from_hex('#FF007F'))
        layout.add_widget(game_title)

        # لعبة PUBG Mobile (مفتوحة تلقائياً)
        layout.add_widget(Label(text="PUBG Mobile: Estimated 60 FPS (Smooth/High)", font_size='14sp'))
        pubg_bar = ProgressBar(max=100, value=85)
        layout.add_widget(pubg_bar)

        # لعبة Genshin Impact (مقفلة خلف إعلان بمكافأة)
        self.genshin_label = Label(text="Genshin Impact: [Locked]", font_size='14sp', color=get_color_from_hex('#888888'))
        layout.add_widget(self.genshin_label)
        
        self.unlock_btn = Button(
            text="Watch Ad to Unlock Genshin Impact Stats", 
            background_color=get_color_from_hex('#00FF66'),
            color=get_color_from_hex('#000000'),
            bold=True
        )
        self.unlock_btn.bind(on_press=self.trigger_rewarded_ad)
        layout.add_widget(self.unlock_btn)

        # مساحة فارغة في الأسفل للإعلان السفلي (Banner)
        layout.add_widget(Label(text="[ Persistent Banner Ad Area ]", font_size='12sp', color=get_color_from_hex('#555555')))

        return layout

    def update_fps(self, dt):
        # محاكاة قراءة معدل تحديث الشاشة الفعلي للفريمات
        current_fps = int(Clock.get_fps())
        if current_fps == 0: current_fps = 60
        self.fps_label.text = f"Live FPS: {current_fps}"

    def update_ram(self, dt):
        ram = psutil.virtual_memory()
        available_ram_gb = round(ram.available / (1024 ** 3), 1)
        total_ram_gb = round(ram.total / (1024 ** 3), 1)
        self.ram_label.text = f"Total RAM: {total_ram_gb} GB | Available RAM: {available_ram_gb} GB"

    def trigger_rewarded_ad(self, instance):
        # تشغيل الإعلان وعند اكتماله يتم فتح البيانات
        self.ads.show_rewarded(self.unlock_genshin_data)

    def unlock_genshin_data(self):
        self.genshin_label.text = "Genshin Impact: Estimated 45 FPS (Medium/Stable)"
        self.genshin_label.color = get_color_from_hex('#00FF66')
        self.unlock_btn.disabled = True
        self.unlock_btn.text = "Unlocked Successfully"

if __name__ == '__main__':
    GamerXPulseApp().run()
