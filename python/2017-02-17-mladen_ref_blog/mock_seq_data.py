
def gen_seq_from_number(length, last_used):
        return str(last_used).zfill(length)

l = {}


l[2] = ['kG', 'KF', 'xu', 'Qj', 'Cv', 'SV', 'Ms', 'ON', 'sJ', 'RV', 'xE', 'kX', 'kO', 'Qw', 'XJ', 'vk', 'Bn', 'rI',
        'lO', 'YU', 'PE', 'sK', 'gc', 'Xl', 'IU', 'jR', 'am', 'If', 'mu', 'Jj', 'bF', 'GD', 'Mb', 'Ml', 'OB', 'iW',
        'rE', 'ZN', 'Pw', 'tV', 'hs', 'CP', 'wq', 'tx', 'lw', 'Hw', 'GL', 'Al', 'vV', 'tZ', 'Pb', 'go', 'Ou', 'Vq',
        'lk', 'GB', 'Yy', 'Fw', 'Nw', 'WI', 'WA', 'Ku', 'TW', 'AK', 'wm', 'BO', 'QN', 'ZQ', 'ps', 'bh', 'MT', 'GV',
        'tc', 'Jg', 'ME', 'HJ', 'UL', 'qY', 'jt', 'rN', 'ak', 'aj', 'bD', 'EX', 'bP', 'Zn', 'qL', 'os', 'UF', 'lz',
        'no', 'ei', 'HT', 'Os', 'gx', 'Yx', 'wv', 'nx', 'eV', 'ZG']
l[3] = ['dfu', 'wEs', 'AcX', 'YJN', 'CuQ', 'MvT', 'NAu', 'RdI', 'etl', 'QIo', 'LgD', 'lBi', 'ojL', 'lbV', 'LbJ',
        'tuO', 'Tnd', 'VBH', 'VrP', 'Qst', 'YuX', 'Sop', 'QBj', 'MIF', 'NeI', 'LDj', 'LXb', 'ZUx', 'fqs', 'aou',
        'KNj', 'pNe', 'Dgp', 'fUn', 'pim', 'nDf', 'SrI', 'QEl', 'Cou', 'XVr', 'ZpM', 'Rhz', 'wpv', 'TEJ', 'JAT',
        'EkP', 'qtO', 'ZMc', 'zYl', 'HUZ', 'ZMT', 'qPd', 'Rql', 'MDp', 'usB', 'paA', 'OYi', 'ESN', 'jvm', 'ocU',
        'sNb', 'GZt', 'FUB', 'Ick', 'LYi', 'feo', 'jMK', 'KTc', 'czK', 'iXU', 'qwl', 'Vcf', 'xce', 'Kyb', 'ATG',
        'QTz', 'hBp', 'jaG', 'JXx', 'vPo', 'VNa', 'lMI', 'mbu', 'PTQ', 'Zzl', 'ZbF', 'rHM', 'QMW', 'FNS', 'QaN',
        'wEr', 'Rwa', 'PGY', 'Kmf', 'cOR', 'mSM', 'hsY', 'STn', 'gAn', 'dPv']
l[4] = ['FPco', 'tcms', 'OMRJ', 'DQZm', 'zNqO', 'IjRv', 'mBaj', 'txoB', 'Mgkq', 'zwkQ', 'sXaZ', 'FzHj', 'jXBc',
        'uAMB', 'gpQf', 'eXMJ', 'pAyk', 'kxTA', 'ZOmf', 'pkmc', 'VidQ', 'dgYz', 'QTcN', 'AHDh', 'NkFp', 'syBU',
        'sPiG', 'JIdZ', 'oeUX', 'KRzn', 'wiKV', 'SOxr', 'RzmY', 'MTHF', 'uWNj', 'viky', 'PjMr', 'OdmH', 'akDA',
        'sJzK', 'OEPH', 'hbkA', 'zJLU', 'qeFr', 'nxFy', 'bSFn', 'iBrC', 'iEDK', 'RhCD', 'uSKV', 'tFRA', 'cBht',
        'MAvH', 'qpnC', 'FIaT', 'lbAt', 'oJKL', 'Rswu', 'NhFn', 'euYS', 'OhlA', 'ychZ', 'gDbA', 'IXUm', 'vVfm',
        'CMVI', 'oAxV', 'CIcG', 'ICha', 'AvRr', 'xOrQ', 'snmB', 'Kcuo', 'jYSO', 'LHwQ', 'ufcY', 'BGKA', 'Ysyr',
        'SHwp', 'fFSZ', 'AsWq', 'trHW', 'BqGi', 'uZcn', 'nWzy', 'ZzNb', 'dtYO', 'FRls', 'aDWp', 'CUVz', 'EkLQ',
        'gfwX', 'dkZG', 'GQSz', 'kUGK', 'FZJn', 'ghos', 'MJCN', 'LRZc', 'tCRG']
l[5] = ['KrJZv', 'lYkED', 'tbPLC', 'TlkMG', 'bReGz', 'FmBfU', 'qDdNF', 'PRSIq', 'HinpO', 'RzMZb', 'MVKAz', 'jvSVT',
        'vIVru', 'pdrHD', 'tKrBf', 'YaDZf', 'oZzQt', 'RScdw', 'IjvRn', 'ixhoa', 'Udthy', 'FuIXL', 'wbrXM', 'CXVUT',
        'tKbIZ', 'AHCjf', 'xCJlH', 'plLKm', 'yeFqX', 'bZBYg', 'zcKXD', 'vYfGy', 'wnaoV', 'GWCDe', 'CNpEU', 'WvLTz',
        'pbBwu', 'vMhBn', 'LUVWP', 'YKICd', 'oTsyz', 'mFYVy', 'CJtvd', 'Mqwsn', 'eUEXa', 'mXfTk', 'rnVcp', 'hWkJd',
        'cJziN', 'rMlDE', 'fMyjC', 'Xersw', 'wFZlH', 'mbQqh', 'hoCgI', 'rNuFV', 'lhPVy', 'CpYmV', 'sIcMQ', 'YtgOk',
        'WovAk', 'CHegf', 'lyfzA', 'FkfTN', 'qNmBC', 'KEiqJ', 'NAlGv', 'mdiyj', 'QsSBf', 'DsrlX', 'nJoKl', 'vlQSz',
        'hvxAg', 'vrmPa', 'XnLMP', 'hYPzt', 'ceDgz', 'yJpMb', 'yxmjI', 'DVxPl', 'yeljx', 'wIpXB', 'tgwiL', 'idDqY',
        'AhtEB', 'jZNrq', 'WUNoe', 'GxNaA', 'UjrLN', 'aTKNo', 'GaDgr', 'zelCb', 'SuVhr', 'Hyuat', 'BrFMh', 'EFIKY',
        'QWkum', 'lByiE', 'flxya', 'KemOC']
l[6] = ['AEZnpd', 'KEoRUV', 'iJxDpI', 'QVBugF', 'NgokCV', 'vmajLB', 'SYOabs', 'DEBZNG', 'ayJwsK', 'ujHIYl', 'ZKcAmU',
        'tHVTDy', 'trYqcR', 'HXjCFS', 'ThmSdr', 'hCiGXo', 'fxcYLa', 'rREQiK', 'iUjfez', 'tmZHXf', 'TejuWC', 'ZOSXGE',
        'JGVFQO', 'IasBjW', 'wVQAKi', 'zwGAWS', 'iqFsyz', 'ExVBeX', 'tRekYP', 'bGocwx', 'wXlbzH', 'pPtYzZ', 'uifIXP',
        'cohsiO', 'tGYSdf', 'mFkJhd', 'AouneG', 'hwAIqN', 'cRJtNA', 'jMBbSi', 'gkoqNT', 'tOervd', 'FCzxpi', 'PVIEwJ',
        'xnZNmg', 'tBVwdW', 'fcSQGe', 'biKaUW', 'wmeiXD', 'HOLCUn', 'RWaISf', 'JVoKrz', 'gIiQhX', 'jrPSRe', 'afojSB',
        'ZLyXct', 'BloPsD', 'hAUzZR', 'zELjsB', 'aJYSpU', 'GKdFMj', 'OeXxVo', 'nKgOuQ', 'DtbhTs', 'gebUEn', 'UPdeYp',
        'sbmnvh', 'cjePvW', 'brTDxt', 'WkIrcJ', 'pjOQSt', 'ZvOmBM', 'LbVCoK', 'gRGpYU', 'GRIEkU', 'cdFkob', 'mRxGfv',
        'BrUMRY', 'HGIYSV', 'BPGdvf', 'gvNVEs', 'Ueuycb', 'XMmihK', 'UMeEFp', 'eBrWgy', 'nZwIjE', 'CeQMLR', 'bmTXoQ',
        'hZDEFW', 'gzQKbt', 'zoqvCH', 'bcLhOC', 'mCNAMJ', 'jzGwSu', 'VhObGe', 'KUBzYb', 'UcjNtI', 'zebcOq', 'ELxOBf',
        'kCavHT']
l[7] = ['yAsUZim', 'LhCuqTM', 'WEmVwUx', 'WmuRvMc', 'cYteZpJ', 'OZKJADy', 'uvfRZLD', 'LXyzjou', 'PsQGIcJ', 'rWQIHbw',
        'zBVTyDJ', 'xzmXBAg', 'YJklGOd', 'YfHcjOp', 'OcDCMHQ', 'YmnbwBS', 'pucnYeB', 'CJBPSOk', 'XtMPvfh', 'cikaTDe',
        'GSPosVb', 'Qjuqlac', 'CifprYQ', 'KYymbJg', 'yjaSwvI', 'kFuxagc', 'rEKUSAe', 'DCJdHVR', 'lWsLipm', 'MKBtDks',
        'gCLwnZX', 'UcmFrTS', 'yUDdVjF', 'bgfAudr', 'wFEcubS', 'bPxDKHE', 'hGlFBKb', 'COpGRyM', 'OdLRsun', 'ITLypNc',
        'rGQBvYO', 'RbHfUqD', 'iRcTXVB', 'kBRPnAl', 'TrqpwcK', 'BOKsgvG', 'tpfWAcU', 'pYGfKui', 'JujpMkc', 'HozTwvk',
        'cYFZOCv', 'NJGkaqy', 'HufOEmS', 'AvYbynX', 'wolpTbE', 'loedFrV', 'XCjwtZN', 'WGrPlJw', 'SsMcIuD', 'VQybfUs',
        'ZjwyIhF', 'nTUAexl', 'GyvJhSm', 'zIJUVDC', 'fQlgyFq', 'lpXryKT', 'nbhlcJQ', 'cwTBLyY', 'CvbMENl', 'mipbSkQ',
        'XRWiHEv', 'AaPrJDZ', 'ztYoIyE', 'SRFlnwc', 'WIqgFOv', 'RBbNpxl', 'DfNlgQM', 'VxzkWbA', 'eguJFAw', 'cNfWPKG',
        'GLMfzNn', 'yjVORlp', 'SjrNhGZ', 'bDxrFcS', 'ynuNHMU', 'KujNzYT', 'ywNnOum', 'haYfGEF', 'xDaRgvh', 'fqicDyR',
        'lkughFb', 'oQezIqS', 'TVRBCug', 'kCTKxSs', 'NDUMoPE', 'eXxBZGH', 'VfIJpdg', 'IHkAmSU', 'ZhyLseT', 'sIwnCmQ']
