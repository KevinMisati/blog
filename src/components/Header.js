import React from 'react'
import { 
    AppBar,
    Toolbar,
    Typography,
    CssBaseline
} 
    from '@mui/material'
    import { makeStyles } from '@mui/styles';

    const useStyles = makeStyles((theme) => ({
        appBar: {
            // borderBottom: `1px solid ${theme.palette.divider}`,
        },
        }));

const Header = () => {
    const classes = useStyles()
return (
    <>
        <CssBaseline />
        <AppBar 
            position='static'
            color='white'
            elevation={0}
            className={classes.appBar}
        >
            <Toolbar>
                <Typography variant='h6' color='inherit' noWrap>
                    BlogmeUp
                </Typography>
            </Toolbar>
        </AppBar>
    </>
  )
}

export default Header