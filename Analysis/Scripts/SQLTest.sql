SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR,SectOptData.IRIAV 
FROM Options o
	INNER JOIN OptionEconomics oe
		ON oe.OPT_ID = o.OPT_ID 
	INNER JOIN SectOptData s
		ON  s.OPT_ID = o.OPT_ID
		
'SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR,SectOptData.IRIAV FROM Options o INNER JOIN OptionEconomics oe ON oe.OPT_ID = o.OPT_ID INNER JOIN SectOptData s	ON  s.OPT_ID = o.OPT_ID'

SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR,SectOptData.IRIAV 
FROM Options,OptionEconomics,SectOptData 
WHERE OPT_ID = o.OPT_ID and OPT_ID = o.OPT_ID

'SELECT Options.OPT_DESC,OptionEconomics.NPV,OptionEconomics.IRR,SectOptData.IRIAV FROM Options,OptionEconomics,SectOptData WHERE OptionEconomics.OPT_ID = Options.OPT_ID and SectOptData.OPT_ID = Options.OPT_ID'