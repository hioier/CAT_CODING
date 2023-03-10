
// DemoDlg.cpp: 实现文件
//

#include "pch.h"
#include "framework.h"
#include "Demo.h"
#include "DemoDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

CDemoDlg* g_dlg;

VOID CALLBACK TimerProc(HWND hwnd, UINT uMsg, UINT_PTR idEvent, DWORD dwTime) {
	int minv, maxv;
	g_dlg->m_progress.GetRange(minv, maxv);

	int pos = g_dlg->m_progress.GetPos();
	pos++;

	if (pos >= maxv) {
		pos = 0;
		::KillTimer(hwnd, 1002);
		g_dlg->m_btn_start_progress.EnableWindow(TRUE);
	}

	g_dlg->m_progress.SetPos(pos);
}

// 用于应用程序“关于”菜单项的 CAboutDlg 对话框

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 对话框数据
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 支持

// 实现
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CDemoDlg 对话框



CDemoDlg::CDemoDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_DEMO_DIALOG, pParent)
	, m_static_show_slider_value(0)
	, m_static_slider(0)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CDemoDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_PROGRESS, m_progress);
	DDX_Control(pDX, IDC_BTN_START_PROGRESS, m_btn_start_progress);
	DDX_Control(pDX, IDC_SLIDER, m_slider);
	//DDX_Control(pDX, IDC_STATIC_SHOW_SLIDER, m_static_show_slider_value);
	DDX_Text(pDX, IDC_STATIC_SHOW_SLIDER, m_static_slider);
}

BEGIN_MESSAGE_MAP(CDemoDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BTN_START_TIMER, &CDemoDlg::OnBnClickedBtnStartTimer)
	ON_BN_CLICKED(IDC_BTN_CLOSE_TIMER, &CDemoDlg::OnBnClickedBtnCloseTimer)
	ON_WM_TIMER()
	ON_BN_CLICKED(IDC_BTN_START_PROGRESS, &CDemoDlg::OnBnClickedBtnStartProgress)
	ON_NOTIFY(NM_CUSTOMDRAW, IDC_SLIDER, &CDemoDlg::OnNMCustomdrawSlider)
END_MESSAGE_MAP()


// CDemoDlg 消息处理程序

BOOL CDemoDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 将“关于...”菜单项添加到系统菜单中。

	// IDM_ABOUTBOX 必须在系统命令范围内。
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作

	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO: 在此添加额外的初始化代码

	g_dlg = this;


	m_progress.SetRange(0, 100);
	m_progress.SetPos(30);
	
	m_slider.SetRange(0, 100);
	m_slider.SetPos(30);

	m_static_slider = 30;
	UpdateData(FALSE);

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}

void CDemoDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CDemoDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CDemoDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



void CDemoDlg::OnBnClickedBtnStartTimer()
{
	SetTimer(1001, 1000, NULL);
}


void CDemoDlg::OnBnClickedBtnCloseTimer()
{
	KillTimer(1001);
}


void CDemoDlg::OnTimer(UINT_PTR nIDEvent)
{
	if (nIDEvent == 1001) {
		CTime now = CTime::GetCurrentTime();
		CString str = now.Format(_T("%Y-%m-%d %H:%M:%S"));

		SetDlgItemText(IDC_STATIC_SHOW_TIME, str);
	}

	CDialogEx::OnTimer(nIDEvent);
}


void CDemoDlg::OnBnClickedBtnStartProgress()
{
	::SetTimer(GetSafeHwnd(), 1002, 10, TimerProc);
	this->m_btn_start_progress.EnableWindow(FALSE);
}


void CDemoDlg::OnNMCustomdrawSlider(NMHDR* pNMHDR, LRESULT* pResult)
{
	LPNMCUSTOMDRAW pNMCD = reinterpret_cast<LPNMCUSTOMDRAW>(pNMHDR);
	
	m_static_slider = m_slider.GetPos();
	UpdateData(FALSE);

	*pResult = 0;
}
