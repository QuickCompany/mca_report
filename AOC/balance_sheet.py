#BALANCE SHEET
EQUITY_AND_LIABILITIES = {
    'shareholders_fund': {
        'share_capital': [],'reserves_and_surplus': [],'money_received': []},
    'share_application_money_pending_allotment': {
        'money_pending': []
    },
    'non_current_liabilities': {'long_term_borrowings': [],'deferred_tax_liabilities_net': [],'other_long_term_liabilities': [],'long_term_provisions': []
    },
    'current_liabilities': {'short_term_borrowings': [],'trade_payables': [],'other_current_liabilities': [],'short_term_provisions': []
    },
    'total' : []
    }

ASSETS = {
    'non_current_assets': {'fixed_assets': [],'non_current_investments': [],'deferred_tax_assets_(net)': [],'long_term_loans_and_advances' : [],'other_non_current_assets' : [],
    },
    'current_assets': {'current_investments': [],'inventories': [],'trade_receivables': [],'cash_and_cash_equivalents' : [],'short_term_loans_and_advances' : [],'other_current_assets' : [],
    },
    'total' : []
    }

FIXED_ASSETS = {
    'tangible_assets': [],
    'intangible_assets': [],
    'capital_work_in_progress': [],
    'intangible_assets_under_development' : [],
    }

def balance_sheet(value_element,text):

    desired_value = value_element
    object_element = desired_value.getparent()
    dict_elements = object_element.findall('.//string')

    if len(dict_elements) >= 5:
        key = dict_elements[-2].text
        value = dict_elements[-1].text

        if 'ShareCap' in key:
            EQUITY_AND_LIABILITIES['shareholders_fund']['share_capital'].append(value)
        elif 'ResSur' in key:
            EQUITY_AND_LIABILITIES['shareholders_fund']['reserves_and_surplus'].append(value)
        elif 'ShareWarrant' in key:
            EQUITY_AND_LIABILITIES['shareholders_fund']['money_received'].append(value)
        elif 'ShareAllot' in key:
            EQUITY_AND_LIABILITIES['share_application_money_pending_allotment']['money_pending'].append(value)
        elif 'LongTerm' in key:
            EQUITY_AND_LIABILITIES['non_current_liabilities']['long_term_borrowings'].append(value)
        elif 'DefLiabl' in key:
            EQUITY_AND_LIABILITIES['non_current_liabilities']['deferred_tax_liabilities_net'].append(value)
        elif 'LongLiabl' in key:
            EQUITY_AND_LIABILITIES['non_current_liabilities']['other_long_term_liabilities'].append(value)
        elif 'LongProv' in key:
            EQUITY_AND_LIABILITIES['non_current_liabilities']['long_term_provisions'].append(value)
        elif 'ShortBorrow' in key:
            EQUITY_AND_LIABILITIES['current_liabilities']['short_term_borrowings'].append(value)
        elif 'CurrentLiabl' in key:
            EQUITY_AND_LIABILITIES['current_liabilities']['other_current_liabilities'].append(value)
        elif 'ShortProv' in key:
            EQUITY_AND_LIABILITIES['current_liabilities']['short_term_provisions'].append(value)

        elif 'NonCurrent' in key:
            ASSETS['non_current_assets']['non_current_investments'].append(value)
        elif 'DefTax' in key:
            ASSETS['non_current_assets']['deferred_tax_assets_(net)'].append(value)
        elif 'LongLoan' in key:
            ASSETS['non_current_assets']['long_term_loans_and_advances'].append(value)
        elif 'CurrentP' in key:
            ASSETS['current_assets']['current_investments'].append(value)
        elif 'Inventory' in key:
            ASSETS['current_assets']['inventories'].append(value)
        elif 'Cash' in key:
            ASSETS['current_assets']['cash_and_cash_equivalents'].append(value)
        elif 'ShortLoan' in key:
            ASSETS['current_assets']['short_term_loans_and_advances'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row26[0].OtherAsset" in text:
        ASSETS['non_current_assets']['other_non_current_assets'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row33[0].OtherAsset" in text:
        ASSETS['current_assets']['other_current_assets'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row19[0].TangAsset" in text:
        FIXED_ASSETS['tangible_assets'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row20[0].IntangAsset" in text:
        FIXED_ASSETS['intangible_assets'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row21[0].CapWork" in text:
        FIXED_ASSETS['capital_work_in_progress'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row22[0].IntangAsset" in text:
        FIXED_ASSETS['intangible_assets_under_development'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row34[0].Total" in text:
        ASSETS['total'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row15[0].Total" in text:
        EQUITY_AND_LIABILITIES['total'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row12[0].Trade" in text:
        EQUITY_AND_LIABILITIES['current_liabilities']['trade_payables'].append(value)

    if text and ".BalanceSheet1_PartB[0].Table6[0].Row30[0].Trade" in text:
        ASSETS['current_assets']['trade_receivables'].append(value)

    ASSETS['non_current_assets']['fixed_assets'].append(FIXED_ASSETS)

    balance_sheet = {'EQUITY_AND_LIABILITIES' : EQUITY_AND_LIABILITIES ,'ASSETS' : ASSETS}

    return balance_sheet
