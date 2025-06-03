import db
import view.dashboard_view as DashboardView

db.init()

def main():
    dashboard = DashboardView.DashboardView()
    dashboard.render()

if __name__ == "__main__":
    main()