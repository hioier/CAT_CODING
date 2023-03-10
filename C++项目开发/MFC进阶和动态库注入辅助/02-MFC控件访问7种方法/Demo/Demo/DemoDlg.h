
// DemoDlg.h: 头文件
//

#pragma once


// CDemoDlg 对话框
class CDemoDlg : public CDialogEx
{
// 构造
public:
	CDemoDlg(CWnd* pParent = nullptr);	// 标准构造函数

// 对话框数据
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_DEMO_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 支持


// 实现
protected:
	HICON m_hIcon;

	// 生成的消息映射函数
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedButtonAdd1();
	afx_msg void OnBnClickedButtonAdd2();
	afx_msg void OnBnClickedButtonAdd3();
	
public:
	afx_msg void OnBnClickedButtonAdd4();
private:
	CEdit m_edit_contral_a;
	CEdit m_edit_contral_b;
	CEdit m_edit_contral_c;

	int m_edit_int_a;
	int m_edit_int_b;
	int m_edit_int_c;
public:
	afx_msg void OnBnClickedButtonAdd5();
	afx_msg void OnBnClickedButtonAdd6();
	afx_msg void OnBnClickedButtonAdd7();
};
