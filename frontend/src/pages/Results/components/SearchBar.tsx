import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import { Grid, IconButton, Link, TextField, Typography } from '@mui/material'
import React, { FunctionComponent, useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'
import useLayoutsStyles from 'src/assets/layout'
import { Micro } from 'src/components'

interface Props {
    onFinalTranscript: (transcript: string) => void
    returnWrittenText: (writtenText: string) => void
}

const SearchBar: FunctionComponent<Props> = ({ onFinalTranscript, returnWrittenText }) => {
    const styles = useLayoutsStyles()
    const { t } = useTranslation()

    const [transcript, setTranscript] = useState('')
    const [writtenText, setWrittenText] = useState<{ departure: string; destination: string }>({
        departure: '',
        destination: '',
    })

    useEffect(() => {
        returnWrittenText(`${writtenText.departure} ${writtenText.destination}`)
    }, [returnWrittenText, writtenText, t])

    return (
        <Grid container className={styles.container_searchbar}>
            <Grid item xs={12}>
                <Typography variant="h2" component="div" gutterBottom className={styles.title}>
                    {t('research')}
                </Typography>
            </Grid>
            <Grid item xs={6}>
                <TextField
                    sx={{ input: { color: 'white' } }}
                    fullWidth
                    label={t('departure')}
                    id="starting-point"
                    variant="outlined"
                    color="primary"
                    onChange={event =>
                        setWrittenText(old => ({
                            ...old,
                            departure: event.target.value.length
                                ? `${t('from')} ${event.target.value[0].toUpperCase() + event.target.value.slice(1)}`
                                : '',
                        }))
                    }
                    InputLabelProps={{
                        classes: {
                            root: styles.cssLabel,
                        },
                    }}
                />
            </Grid>
            <Grid item xs={6}>
                <TextField
                    sx={{ input: { color: 'white' } }}
                    fullWidth
                    label={t('destination')}
                    id="end-point"
                    variant="outlined"
                    color="primary"
                    onChange={event =>
                        setWrittenText(old => ({
                            ...old,
                            destination: event.target.value.length
                                ? `${t('to')} ${event.target.value[0].toUpperCase() + event.target.value.slice(1)}`
                                : '',
                        }))
                    }
                    InputLabelProps={{
                        classes: {
                            root: styles.cssLabel,
                        },
                    }}
                />
            </Grid>
            <Grid item xs={6} className={styles.align_item}>
                <Micro onFinalTranscript={setTranscript} />
            </Grid>
            <Grid item xs={6} className={styles.align_item}>
                <IconButton color="primary" component={Link} onClick={() => onFinalTranscript(transcript)}>
                    <Link>
                        <ArrowForwardIcon color="primary" />
                    </Link>
                </IconButton>
            </Grid>
        </Grid>
    )
}
export default SearchBar
